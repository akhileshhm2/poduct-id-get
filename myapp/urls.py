from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path("remove_cart/<int:cart_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart_update/<int:cart_id>/", views.cart_update, name="cart_update"),
    path("billing/", views.billing_page, name="billing"),
    path("order_success/", views.order_success, name="order_success"),
]

