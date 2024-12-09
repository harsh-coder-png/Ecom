from django.urls import path
from . import views

urlpatterns = [
    path('',views.showcart,name='showcart'),
    path('addtocart',views.cart),
    path('deletefromcart',views.deletefromcart)

]