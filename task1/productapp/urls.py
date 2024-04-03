from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.productlist, name="productlist1"),
    path('',views.productdetail, name="productdetail1"),
]