from django.shortcuts import render, redirect
from .forms import SignUpForm ,LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    msg = None
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html',{'form':form, 'msg': msg})
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            Username = form.cleaned_data.get('Username')
            password = form.cleaned_data.get('password')
            User = authenticate(Username=Username, password=password)
            if User is not None and user.is_user:
                login(request, User)
                return redirect('user')
            elif user is not None and user.is_dealer:
                login(request, User)
                return redirect('dealer')

            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request,'login.html',{'form':form, 'msg':msg})

def user(request):
    return render(request,'user.html')

def dealer(request):
    return render(request,'dealer.html')
