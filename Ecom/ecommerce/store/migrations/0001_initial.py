# Generated by Django 4.2.6 on 2024-09-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ImageField(default='', upload_to='store')),
            ],
        ),
    ]
