from .models import Products
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import ReadOnlyField


# class ReadUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id","username","first_name","last_name")
#         ReadOnlyField = fields

class WirteProductSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Products
        fields = ("name","sku_id","description","is_active")
    

class ReadProductSerializer(serializers.ModelSerializer):
    # user = ReadUserSerializer()
    class Meta:
        model = Products
        fields = ("id","name","sku_id","description","is_active")
        ReadOnlyField = fields 
