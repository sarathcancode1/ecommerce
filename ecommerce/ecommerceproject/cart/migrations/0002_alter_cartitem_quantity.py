# Generated by Django 4.1.5 on 2023-01-13 13:25

from django.db import migrations, models
import ecomapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(verbose_name=ecomapp.models.Product),
        ),
    ]