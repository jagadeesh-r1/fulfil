from .celery import app
from product_importer.models import Products
from django.db import transaction
from django.contrib.auth.models import User


# @app.task
# def add_data_to_db(reader):
#     objs = [
#     Products(
#         user = User,
#         name = row['name'],
#         sku_id = row['sku'],
#         description = row['description'] 
#     )
#     for row in reader
#     ]

#     with transaction.atomic():
#         Products.objects.bulk_create(objs)