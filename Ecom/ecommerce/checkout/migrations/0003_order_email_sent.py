# Generated by Django 5.1 on 2024-10-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_placed'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
    ]
