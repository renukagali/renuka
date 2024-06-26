from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('user_home/', views.user_home, name='user_home'),
    path('product_list/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('updateproduct/<int:product_id>/', views.updateproduct, name='updateproduct'),
    path('deleteProduct/<int:product_id>/', views.deleteProduct, name='deleteProduct'),
    path('deletewishlist/<int:wishlist_id>/', views.deletewishlist, name='deletewishlist'),
    path('addwishlist/<int:product_id>/', views.addwishlist, name='addwishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('updateuserdetails/', views.updateuserdetails, name='updateuserdetails'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('categorylist/', views.categorylist, name='categorylist'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('updatecategory/<int:category_id>/', views.updatecategory, name='updatecategory'),
    path('deletecategory/<int:category_id>/', views.deletecategory, name='deletecategory'),

    path('addcart/<int:product_id>/', views.addcart, name='addcart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('deletefromcart/<int:cart_item_id>/', views.deletefromcart, name='deletefromcart'),



    
]
