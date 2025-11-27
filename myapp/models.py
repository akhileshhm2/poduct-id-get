
# Create your models here.
from django.db import models

# Product model for storing product info
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    

    # optional: for extra features

    def __str__(self):
        return self.name

class Cartitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
from django.db import models
from django.contrib.auth.models import User

# class BillingDetails(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

#     full_name = models.CharField(max_length=150)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)

#     country = models.CharField(max_length=100)
#     address = models.TextField()
#     city = models.CharField(max_length=100)
#     postal_code = models.CharField(max_length=20)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.full_name} - {self.email}"
    
# class Order(models.Model):
#     billing_details = models.ForeignKey(BillingDetails, on_delete=models.CASCADE)
    
#     subtotal = models.DecimalField(max_digits=10, decimal_places=2)
#     shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     total = models.DecimalField(max_digits=10, decimal_places=2)

#     is_paid = models.BooleanField(default=False)
#     order_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order #{self.id} - {self.billing_details.full_name}"

class BillingDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    country = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# --------------------------
# ORDER MODEL
# --------------------------
class Order(models.Model):
    billing_details = models.ForeignKey(BillingDetails, on_delete=models.CASCADE)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    is_paid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
    
    from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    country = models.CharField(max_length=100, blank=True, null=True)

    # Add more custom fields easily:
    # phone = models.CharField(max_length=15, blank=True, null=True)
    # address = models.TextField(blank=True, null=True)
    # date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.email


