# Generated by Django 3.2.5 on 2021-07-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sku_id', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
