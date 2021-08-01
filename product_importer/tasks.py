import requests
import pandas as pd
from .models import Products
from celery import shared_task
from django.db import transaction

webhook_urls = []

@shared_task
def add_data_to_db(reader):
    data = pd.DataFrame([sub.split(",") for sub in reader])
    data.columns = ["name","sku","description"]
    data.drop_duplicates(subset ="sku",keep = False, inplace = True)
    data = data[data['sku']!="None"]
    objs = [
    Products(
        name = data['name'][ind],
        sku_id = data['sku'][ind],
        description = data['description'][ind] 
    )
    for ind in data.index
    ]

    with transaction.atomic():
        Products.objects.bulk_create(objs,ignore_conflicts=True)

@shared_task
def send_triggers():
    # print(webhook_urls)
    for i in webhook_urls:
        print(requests.post(i,{}))