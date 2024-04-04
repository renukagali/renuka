# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('user_home/', views.user_home, name='user_home'),
    path('product_list/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('updateproduct/', views.updateproduct, name='aupdateproduct'),
    path('deleteProduct/', views.deleteProduct, name='deleteProduct'),
    path('deletewishlist/', views.deletewishlist, name='deletewishlist'),
    path('updatewishlist/', views.updatewistlist, name='updatewishlist'),
    path('addwishlist/', views.addwishlist, name='addwishlist'),

    
]
