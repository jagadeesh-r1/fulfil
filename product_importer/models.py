from django.db import models
import random
from django.contrib.auth.models import User

from django.db.models.expressions import Value

# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="Products")
    name = models.CharField(max_length=50,blank=False)
    sku_id = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    is_active = models.IntegerField(blank=False,default=random.choice([0,1]))