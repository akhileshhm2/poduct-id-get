# # from django.shortcuts import redirect,render,get_object_or_404
# # from. models import Product
# # from . models import Cartitem
# # from .forms import DeliveryDetailsForm

# # View to render the product page
# # def product_list(request):
# #     uploads = Product.objects.all()
# #     return render(request,'men.html',{'uploads':uploads})

# # def product_details(request,product_id):
# #     upload=get_object_or_404(Product,id=product_id)   
# #     return render(request, 'product_details.html', {'upload': upload})

# # # Create your views here.
# # def cart(request):
# #     cart_items=Cartitem.objects.all()
# #     total_amount=sum(item.total_price for item in cart_items)
# #     return render(request,'cart.html',{
# #         'cart_items':cart_items,
# #         'total_amount':total_amount

# #     })

# # def add_to_cart(request,product_id):
# #     product=get_object_or_404(Product,id=product_id)
# #     cart_item,created=Cartitem.objects.get_or_create(product=product)

# #     if not created:
# #         cart_item.quantity +=1
# #         cart_item.save()

# #     return redirect('cart')
# # from django.shortcuts import redirect, render, get_object_or_404
# # from .models import Product, Cartitem

# from django.shortcuts import redirect, render, get_object_or_404
# from django.contrib import messages

# from .models import Product, Cartitem, BillingDetails, Order
# from .forms import DeliveryDetailsForm
# def product_list(request):
#     uploads = Product.objects.all()
#     return render(request, 'men.html', {'uploads': uploads})


# def product_details(request, product_id):
#     upload = get_object_or_404(Product, id=product_id)
#     return render(request, 'product_details.html', {'upload': upload})


# def cart(request):
#     cart_items = Cartitem.objects.all()
#     total_amount = sum(item.total_price for item in cart_items)

#     return render(request, 'cart.html', {
#         'cart_items': cart_items,     # FIXED NAME
#         'total_amount': total_amount  # FIXED NAME
#     })


# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     cart_item, created = Cartitem.objects.get_or_create(product=product)

#     if created:
#         cart_item.quantity = 1      # FIX: Set initial quantity
#     else:
#         cart_item.quantity += 1     # Increase if exists

#     cart_item.save()

#     return redirect('cart')

# def cart_update(request,cart_id):
#     cart_item= get_object_or_404(Cartitem,id=cart_id)
#     if request.method=='POST':
#         quantity=int(request.POST.get("quantity",1))
#         if quantity > 0:
#             cart_item.quantity=quantity
#             cart_item.save()
#         else:
#             cart_item.delete
#     return redirect('cart')


# def remove_from_cart(request,cart_id):
#     cart_item=get_object_or_404(Cartitem,id=cart_id)
#     cart_item.delete()
#     return redirect('cart')

# # from django.shortcuts import render, redirect
# # from django.contrib import messages

# # from .models import BillingDetails, Order


# # def billing_page(request):

# #     if request.method == "POST":
# #         full_name = request.POST.get("full_name")
# #         email = request.POST.get("email")
# #         phone = request.POST.get("phone")
# #         country = request.POST.get("country")
# #         address = request.POST.get("address")
# #         city = request.POST.get("city")
# #         postal_code = request.POST.get("postal_code")

# #         # ✅ Save billing details
# #         billing = BillingDetails.objects.create(
# #             user=request.user if request.user.is_authenticated else None,
# #             full_name=full_name,
# #             email=email,
# #             phone=phone,
# #             country=country,
# #             address=address,
# #             city=city,
# #             postal_code=postal_code
# #         )

# #         # ✅ Create order (hardcoded totals — replace later with cart)
# #         order = Order.objects.create(
# #             billing_details=billing,
# #             subtotal=118.00,
# #             shipping=6.00,
# #             tax=4.00,
# #             total=128.00
# #         )

# #         messages.success(request, "Order placed successfully!")
# #         return redirect("order_success")  # ✅ create this URL
    

# #     return render(request, "billing_details.html")
# # from .forms import DeliveryDetailsForm
# def billing_page(request):

#     # Fetch all cart items
#     cart_items = Cartitem.objects.all()

#     # Calculate totals dynamically
#     subtotal = sum(item.total_price for item in cart_items)
#     shipping = 6.00
#     tax = 4.00
#     total = subtotal + shipping + tax

#     if request.method == "POST":
#         form = DeliveryDetailsForm(request.POST)

#         if form.is_valid():
#             # Save billing data
#             billing = form.save(commit=False)
#             billing.user = request.user if request.user.is_authenticated else None
#             billing.save()

#             # Create Order
#             Order.objects.create(
#                 billing_details=billing,
#                 subtotal=subtotal,
#                 shipping=shipping,
#                 tax=tax,
#                 total=total
#             )

#             # Clear cart after order
#             cart_items.delete()

#             messages.success(request, "Order placed successfully!")
#             return redirect('order_success')

#     else:
#         form = DeliveryDetailsForm()

#     return render(request, "billing_details.html", {
#         "form": form,
#         "subtotal": subtotal,
#         "shipping": shipping,
#         "tax": tax,
#         "total": total
#     })


# # ---------------------------------------------------
# # ORDER SUCCESS PAGE
# # ---------------------------------------------------
# def order_success(request):
#     return render(request, "order_success.html")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Product, Cartitem, BillingDetails, Order
from .forms import DeliveryDetailsForm
from decimal import Decimal
from django.contrib.auth.decorators import login_required



# ---------------------------------------------------
# PRODUCT LIST PAGE
# ---------------------------------------------------
def product_list(request):
    uploads = Product.objects.all()
    return render(request, 'men.html', {'uploads': uploads})


# ---------------------------------------------------
# PRODUCT DETAILS PAGE
# ---------------------------------------------------
def product_details(request, product_id):
    upload = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'upload': upload})


# ---------------------------------------------------
# CART PAGE
# ---------------------------------------------------
@login_required(login_url='signin')
def cart(request):
    # cart_items = Cartitem.objects.all()
    cart_items = Cartitem.objects.filter(user=request.user)
    total_amount = sum(item.total_price for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_amount': total_amount
    })


# ---------------------------------------------------
# ADD TO CART
# ---------------------------------------------------
@login_required(login_url='signin')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cartitem.objects.get_or_create(product=product,user=request.user)

    if created:
        cart_item.quantity = 1
    else:
        cart_item.quantity += 1

    cart_item.save()

    return redirect('cart')


# ---------------------------------------------------
# UPDATE CART ITEM
# ---------------------------------------------------
@login_required(login_url='sigin')
def cart_update(request, cart_id):
    cart_item = get_object_or_404(Cartitem, id=cart_id)

    if request.method == 'POST':
        quantity = int(request.POST.get("quantity", 1))

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart')


# ---------------------------------------------------
# REMOVE FROM CART
# ---------------------------------------------------
@login_required(login_url='signin')
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cartitem, id=cart_id)
    cart_item.delete()
    return redirect('cart')


# ---------------------------------------------------
# BILLING PAGE + ORDER PROCESSING
# ---------------------------------------------------
@login_required(login_url='signin')
def billing_page(request):
    cart_items = Cartitem.objects.filter(user=request.user)

    cart_items = Cartitem.objects.all()

    # Calculate dynamic totals
    subtotal = Decimal(sum(item.total_price for item in cart_items))
    shipping = Decimal("6.00")
    tax = Decimal("4.00")
    total = subtotal + shipping + tax

    if request.method == "POST":
        form = DeliveryDetailsForm(request.POST)

        if form.is_valid():

            # Save customer details
            billing = form.save(commit=False)
            billing.user = request.user if request.user.is_authenticated else None
            billing.save()

            # Create order
            Order.objects.create(
                user=request.user,
                billing_details=billing,
                subtotal=subtotal,
                shipping=shipping,
                tax=tax,
                total=total
            )

            # Clear cart
            cart_items.delete()

            messages.success(request, "Order placed successfully!")
            return redirect('order_summary')

    else:
        form = DeliveryDetailsForm()

    return render(request, "billing_details.html", {
        "form": form,
        "subtotal": subtotal,
        "shipping": shipping,
        "tax": tax,
        "total": total
    })


# ---------------------------------------------------
# ORDER SUCCESS PAGE
# ---------------------------------------------------
# def order_success(request):
#     latest_order = Order.objects.order_by('-id').first()
#     return render(request, "order_success.html", {
#         'order': latest_order
#     })

import razorpay
from django.conf import settings

@login_required(login_url='signin')
def order_summary(request):
    latest_order = Order.objects.order_by('-id').first()

    if not latest_order:
        messages.error(request, "No order found!")
        return redirect('cart')

    # Razorpay client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Amount must be in PAISA
    razorpay_order = client.order.create({
        "amount": int(latest_order.total * 100),   # convert to paisa
        "currency": "INR",
        "payment_capture": "1"
    })

    context = {
        "order": latest_order,
        "razorpay_order_id": razorpay_order["id"],
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "amount": latest_order.total * 100,  # in paisa for JS
    }

    return render(request, "order_summary.html", context)

from . models import UserProfile
from django.contrib.auth.models import User
    
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        country = request.POST.get("country")    # ← Get country from form

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")
        
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("signup")

        # Create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Create user profile WITH country field
        UserProfile.objects.create(
            user=user,
            country=country
        )

        messages.success(request, "Signup successful! Please login.")
        return redirect("signin")

    return render(request, "signup.html")


from django.contrib.auth import authenticate, login

def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request,username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("product_list")
        else:
            messages.error(request, "Invalid email or password")

    return render(request, "login.html")


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'order_history.html', {'orders': orders})

@login_required(login_url='signin')
def payment_success(request):
    cart_items=Cartitem.objects.filter(user=request.user)
    cart_items.delete()
    return render(request,"payment_success.html")

from .models import Wishlist

@login_required(login_url='signin')
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    messages.success(request, "Added to wishlist!")
    return redirect('wishlist')


@login_required(login_url='signin')
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'items': items})


@login_required(login_url='signin')
def remove_wishlist(request, product_id):
    item = get_object_or_404(Wishlist, user=request.user, product_id=product_id)
    item.delete()
    return redirect('wishlist')

# @login_required(login_url='signin')
# def remove_wishlist(request, product_id):
#     item = Wishlist.objects.filter(user=request.user, product_id=product_id).first()
#     if item:
#         item.delete()
#     return redirect('wishlist')


