# Generated by Django 5.1 on 2024-09-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1, max_length=700),
        ),
    ]
