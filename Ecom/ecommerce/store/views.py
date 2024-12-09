from django.shortcuts import render
from .models import Product
# to avoid using direct links of the website
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    products = Product.objects.all()
    print("Logged in User",request.session.get('username'))
    return render(request,'store/home.html',{'products':products})

@login_required
def search(request):
    context = {}
    if request.method == 'POST':
        pid = request.POST.get('pid')
        products = Product.objects.filter(name__contains = pid )
        context['products'] = products
    return render(request,'store/search.html',context)  