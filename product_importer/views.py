# from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .serializers import ReadProductSerializer, WirteProductSerializer
from .models import Products
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class ProductModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("id","sku_id","description","is_active")
    ordering_fields = ("sku_id","is_active")
    filterset_fields = ()

    def get_queryset(self):
        return Products.objects.select_related("user").filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list","retrieve"):
            return ReadProductSerializer

        return WirteProductSerializer
