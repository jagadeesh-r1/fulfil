from os import name
from django.urls import path
from . import views
from django.urls.conf import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()

router.register(r'products',views.ProductModelViewSet,basename="product-detail")

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_auth_token,name="obtain-auth-token"),
    path('upload/',views.upload_file,name="upload csv")
] + router.urls