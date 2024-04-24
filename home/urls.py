from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('shop/',views.shop, name='shop'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('',views.login_fun, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout_fun, name='logout'),
    path('cart/',views.cart_info, name='cart'),
    path('user/',views.user, name='user'),
    path('upload/',views.upload, name='upload'),
    path('edit/',views.edit, name='edit'),
    path('addtocart/<int:ids>',views.addtocart, name='addtocart'),
    path('addorder/<int:ids>',views.addorder, name='addorder'),
    path('deletecart/<int:ids>',views.deletecart, name='removecart'),
    path('order/',views.order_info, name='order'),
    path('deleteorder/<int:ids>',views.deleteorder, name='removeorder'),
]