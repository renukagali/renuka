from django.shortcuts import render
from .models import Product

# Create your views here.
def productlist(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def productdetail(request, primarykey):
    product = Product.objects.get(primarykey=primarykey)
    return render(request, 'product_detail.html', {'product': product})

def wish_list(request):
    return render(request,'wishlist.html',{'wishlist': wish_list})