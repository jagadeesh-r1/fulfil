import random
from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50,blank=False)
    sku_id = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    is_active = models.IntegerField(blank=False,default=random.choice([0,1]))   