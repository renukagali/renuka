from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProductForm
from .models import User, Product


def main_home(request):
    return render(request, 'main_home.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = User.Role.DEALER if form.cleaned_data['is_dealer'] else User.Role.USERS
            user.save()
            login(request, user)
            return redirect('add_product' if user.role == User.Role.DEALER else 'user_home')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('add_product' if user.role == User.Role.DEALER else 'user_home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_home(request):
    return render(request, 'user_home.html')


def product_list(request):
    products = Product.objects.filter(dealer=request.user)
    return render(request, 'product_list.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.dealer = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'addproducts.html', {'form': form})

  
#to update a product
def updateproduct(request, id):
    obj = Product.objects.get(pk=id)
    form = ProductForm(instance=obj)
    if request.method =='POST':
        form = ProductForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
    else:
        return render(request,'updateproduct.html',{'form':form})
    

#to delete a product
def deleteProduct(request, id):
    obj = Product.objects.get(pk=id)
    if request.method =='POST':
        obj.delete()
        return redirect('product_list')
    else:
        return render(request,'deleteproduct.html',{'obj':obj})


# def user_home(request):
#     if request.method == 'POST':
#         form = WishlistForm(request.POST)
#         if form.is_valid():
#             Wishlist = form.save(commit=False)
#             Wishlist.user = request.user
#             Wishlist.save()
#             return redirect('Wish_list')
#     else:
#         form = WishlistForm()
#     return render(request,'wishlist_home.html',{'form':form})