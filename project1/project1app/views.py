from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProductForm, WishlistForm, CategoryForm, CartForm
from .models import User, Product, Wishlist, Category, Cart
from django.shortcuts import get_object_or_404
from .forms import UserProfileForm, CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash  
from django.db import IntegrityError


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
            return redirect('product_list' if user.role == User.Role.DEALER else 'user_home')
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
            if user is not None and user.is_active:
                login(request, user)
                if user.role == User.Role.DEALER:
                    return redirect('product_list')
                elif user.dealer_details == 'Category Management User':
                    return redirect('categorylist')
                else:
                    return redirect('user_home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_home(request):
    products = Product.objects.all()
    return render(request, 'user_home.html',{'products':products})



def product_list(request):
    products = Product.objects.filter(dealer=request.user)
    return render(request, 'product_list.html', {'products': products})

#to add product
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
def updateproduct(request, product_id):
    obj = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=obj)
    
    return render(request, 'updateproduct.html', {'form': form})

    

#to delete a product
def deleteProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id) 
    if request.method == 'POST':
        product.delete() 
        return redirect('product_list')
    else:
        return render(request, 'deleteproduct.html', {'product': product})

    

def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    # print(wishlist_items)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})



@login_required
def addwishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    existing_wishlist_item = Wishlist.objects.filter(user=request.user, product=product).first()

    if existing_wishlist_item:
        messages.info(request, 'This item is already in your wishlist.')
        return redirect('wishlist')

    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist_item = form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.product = product
            wishlist_item.save()
            messages.success(request, 'Item added to wishlist successfully.')
            return redirect('wishlist')
    else:
        form = WishlistForm()
    return render(request, 'addwishlist.html', {'form': form, 'product': product})

    

#to delete a wishlist
def deletewishlist(request, wishlist_id):
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id)
    
    if request.method == 'POST':
        wishlist.delete()
        return redirect('wishlist') 
    
    return render(request, 'deletewishlist.html', {'wishlist': wishlist})


def changepassword(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    
    return render(request, 'changepassword.html', {'form': form})


def updateuserdetails(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details were successfully updated!')
            return redirect('user_home')
    else:
        form = UserProfileForm(instance=user)
    
    return render(request, 'updateuserdetails.html', {'form': form})


#to log out
def logout_view(request):
    logout(request)
    return redirect('main_home')


def categorylist(request):
    categories = Category.objects.all()
    return render(request, 'categorylist.html',{'categories': categories})

#to add category
def addcategory(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            return redirect('categorylist')
    return render(request, 'addcategory.html')

# to update category
def updatecategory(request, category_id):
    obj = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('categorylist')
        else:
            form = CategoryForm(instance=obj)
        return render(request, 'updatecategory.html',{'form': form})


# to delete category
def deletecategory(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('categorylist')
    else:
        return render(request, 'deletecategory.html',{'category':category})
    
def categorydetails(request, category_id):
   obj = get_object_or_404(Category, pk=category_id)
   items = Category.objects.all()

   return render (request,'categorydetails.html')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})

# to add cart
def addcart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Quantity updated successfully")
    else:
        messages.success(request, "Product added to your cart")

    return redirect('view_cart')
# to view cart
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})


#delete item from cart
def deletefromcart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Product removed from your cart")
    return redirect('view_cart')




# def lowtohigh(request):
#     products = Product.objects.order_by('price')
#     return render(request, 'sortbyprice.html', {'products': products})

# def hightolow(request):
#     products = Product.objects.order_by('price')
#     return render(request, 'sortbyprice.html', {'products': products})