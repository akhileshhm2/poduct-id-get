from django.contrib import admin

# Register your models here.
from .models import Product,Cartitem
admin.site.register(Product)
admin.site.register(Cartitem)