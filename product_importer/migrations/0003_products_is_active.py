# Generated by Django 2.2.12 on 2021-07-31 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_importer', '0002_auto_20210730_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
