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
    path("order_summary/", views.order_summary, name="order_summary"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout_view, name="logout"),
    path('order_history/', views.order_history, name='order_history'),
    path("payment_success/", views.payment_success, name="payment_success"),

]

