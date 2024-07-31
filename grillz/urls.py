from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.timetable, name='menu'),
    path('review/', views.review, name='review'),
    path('signup/', views.signup, name='signup'),
    path('shop/', views.shop, name='shop'),
    path('add/', views.add_product, name='add_product'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('product_list/', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
