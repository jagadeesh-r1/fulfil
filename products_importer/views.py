# from rest_framework.generics import ListAPIView
import time,datetime
from .models import Products
from django.shortcuts import render
from .tasks import webhook_urls as urls
from django.http import StreamingHttpResponse
from .tasks import add_data_to_db,send_triggers
from rest_framework.viewsets import ModelViewSet
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ReadProductSerializer, WirteProductSerializer

class Home(TemplateView):
    template_name = 'home.html'

class ProductModelViewSet(ModelViewSet):
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("id","sku_id","description","is_active")
    ordering_fields = ("sku_id","is_active")
    filterset_fields = ()

    def get_queryset(self):
        return Products.objects.all()

    def get_serializer_class(self):
        if self.action in ("list","retrieve"):
            return ReadProductSerializer
        if self.action in ("create","partial_update"):
            send_triggers.apply_async((), countdown=1)
        return WirteProductSerializer



@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        decoded_file = uploaded_file.read().decode('utf-8').splitlines()
        print(decoded_file[0])
        return_str = add_data_to_db.apply_async((list(decoded_file),), countdown=1)
        
        def event_stream():
            while return_str.status != 'SUCCESS':
                time.sleep(1)
                print(return_str.status)
                yield 'Data is being imported, The server time is: %s\n\n' % datetime.datetime.now()
            return render(request,'products_redirect.html')
        return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


    return render(request,'base.html')

@csrf_exempt
def delete_products(request):
    if request.method == "POST":
        Products.objects.all().delete()
        return render(request,"base.html")

    return render(request,"deletion.html")


from rest_framework.decorators import api_view

@csrf_exempt
@api_view(["GET","POST"])
def webhooks(request):
    if request.method == "POST":
        webhook_urls = request.data["webhooks"].split(",")
        urls.extend(webhook_urls)
        return render(request,"base.html")

    return render(request,"webhooks.html")
