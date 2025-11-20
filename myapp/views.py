from django.shortcuts import redirect,render,get_object_or_404
from. models import Product
from . models import Cartitem
# View to render the product page
# def product_list(request):
#     uploads = Product.objects.all()
#     return render(request,'men.html',{'uploads':uploads})

# def product_details(request,product_id):
#     upload=get_object_or_404(Product,id=product_id)   
#     return render(request, 'product_details.html', {'upload': upload})

# # Create your views here.
# def cart(request):
#     cart_items=Cartitem.objects.all()
#     total_amount=sum(item.total_price for item in cart_items)
#     return render(request,'cart.html',{
#         'cart_items':cart_items,
#         'total_amount':total_amount

#     })

# def add_to_cart(request,product_id):
#     product=get_object_or_404(Product,id=product_id)
#     cart_item,created=Cartitem.objects.get_or_create(product=product)

#     if not created:
#         cart_item.quantity +=1
#         cart_item.save()

#     return redirect('cart')
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Cartitem


def product_list(request):
    uploads = Product.objects.all()
    return render(request, 'men.html', {'uploads': uploads})


def product_details(request, product_id):
    upload = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'upload': upload})


def cart(request):
    cart_items = Cartitem.objects.all()
    total_amount = sum(item.total_price for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,     # FIXED NAME
        'total_amount': total_amount  # FIXED NAME
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cartitem.objects.get_or_create(product=product)

    if created:
        cart_item.quantity = 1      # FIX: Set initial quantity
    else:
        cart_item.quantity += 1     # Increase if exists

    cart_item.save()

    return redirect('cart')

def cart_update(request,cart_id):
    cart_item= get_object_or_404(Cartitem,id=cart_id)
    if request.method=='POST':
        quantity=int(request.POST.get("quantity",1))
        if quantity > 0:
            cart_item.quantity=quantity
            cart_item.save()
        else:
            cart_item.delete
    return redirect('cart')


def remove_from_cart(request,cart_id):
    cart_item=get_object_or_404(Cartitem,id=cart_id)
    cart_item.delete()
    return redirect('cart')


