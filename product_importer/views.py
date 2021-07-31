# from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .serializers import ReadProductSerializer, WirteProductSerializer
from .models import Products
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .tasks import add_data_to_db
from django.views.decorators.csrf import csrf_exempt
import csv
import time,datetime
from django.http import StreamingHttpResponse


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

        return WirteProductSerializer



@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        print(request.FILES)
        uploaded_file = request.FILES['file']
        print(uploaded_file.name)
        print(uploaded_file.size)
        decoded_file = uploaded_file.read().decode('utf-8').splitlines()
        print(decoded_file[0])
        # reader = csv.DictReader(decoded_file)
        return_str = add_data_to_db.apply_async((list(decoded_file),), countdown=1)
        
        def event_stream():
            while return_str.status != 'SUCCESS':
                time.sleep(1)
                print(return_str.status)
                yield 'Data is being imported, The server time is: %s\n\n' % datetime.datetime.now()
        return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


    return render(request,'base.html')
