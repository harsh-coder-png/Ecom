from django.shortcuts import redirect, render
from store.models import Product
from .models import Cart
from django.contrib.auth.models import User

# Create your views here.
def cart(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        username = User.objects.get(username = request.session.get('username'))
        name = Product.objects.get(id = pid)
        print(name)
        product = Cart.objects.filter(name=name,username__username=username)
        print(product)
        if product:
            for i in product:
                quantity=i.quantity + 1
                total_price=i.total_price * quantity
            Cart.objects.filter(name=name,username__username =username).update(quantity=quantity,total_price=total_price)
        else:
            product = Product.objects.filter(id = pid)   
            
            for p in product:
                price = p.price
                image = p.image
                total_price=p.price
                
            mycart = Cart.objects.create(username = username,name=name,price=price,image = image,total_price=total_price)
            mycart.save()
    return redirect('home')


def showcart(request):
    username = request.session.get('username')
    context = {}
    products = Cart.objects.filter(username__username = username)
    context['products'] = products
    return render(request,'cart/cart.html',context)

def deletefromcart(request):
    username = request.session.get('username')
    if request.method == "POST":
        pname = request.POST.get('pname')
        print(pname)
        product = Product.objects.get(name = pname)
        print(product)
        products = Cart.objects.get(name__name = product, username__username = username)
        print('Deleted')
        products.delete()
    
    return redirect('showcart')



