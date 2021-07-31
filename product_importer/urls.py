from django.urls import path
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()

router.register(r'products',views.ProductModelViewSet,basename="product-detail")

urlpatterns = [
    path('login/', obtain_auth_token,name="obtain-auth-token")
] + router.urls