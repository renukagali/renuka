from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm
from .models import User
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def main_home(request):
    return render(request, 'main_home.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            if form.cleaned_data['is_dealer']:
                user.role = User.Role.DEALER
            user.save()
            login(request, user)
            if user.role == User.Role.USERS:
                return redirect('user_home')
            elif user.role == User.Role.DEALER:
                return redirect('dealer_home')
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
                if user.role == User.Role.USERS:  
                    return redirect('user_home')
                elif user.role == User.Role.DEALER:  
                    return redirect('dealer_home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_home(request):
    return render(request, 'user_home.html')

# def dealer_home(request):
#     return render(request, 'dealer_home.html')


def dealer_home(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.dealer = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_home.html', {'form': form})
    


# def user_home(request):
#     if request.method == 'POST':
#         form = WishlistForm(request.POST)
#         if form.is
#     return render(request,'wishlist.html',{'wishlist': wish_list})
