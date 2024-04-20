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
    path('cart/',views.cart, name='cart'),
    path('user/',views.user, name='user'),
    path('upload/',views.upload, name='upload')
]