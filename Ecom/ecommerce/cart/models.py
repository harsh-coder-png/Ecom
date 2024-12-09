from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.
class Cart(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='store',default='')
    quantity=models.IntegerField(max_length=700,default=1)
    total_price=models.IntegerField(max_length=700,default=0)

    def __str__(self):
        return str(self.username)