from . import views
from django.urls import path
from rest_framework import routers
from django.urls.conf import include
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()

router.register(r'products',views.ProductModelViewSet,basename="product-detail")

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_auth_token,name="obtain-auth-token"),
    path('upload/',views.upload_file,name="upload csv"),
    path('clear_db/',views.delete_products,name="delete products"),
    path('webhooks/',views.webhooks,name="webhooks")
] + router.urls