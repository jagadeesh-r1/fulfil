# Generated by Django 2.2.12 on 2021-07-31 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_importer', '0009_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
        migrations.RemoveField(
            model_name='products',
            name='user',
        ),
        migrations.AlterField(
            model_name='products',
            name='is_active',
            field=models.IntegerField(default=0),
        ),
    ]