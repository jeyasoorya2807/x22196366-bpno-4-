from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Babyproduct, CartItem, Order
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    return render(request, 'babyproducts/index.html')

def product_list(request):
    products = Babyproduct.objects.all()
    return render(request, 'babyproducts/products_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('babyproducts:product_list')
    else:
        form = ProductForm()
    return render(request, 'babyproducts/add_product.html', {'form': form})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    print("cart items=",cart_items)
    return render(request, 'babyproducts/cart.html', {'cart_items': cart_items})


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, f"{cart_item.product.name} has been removed from your cart.")
    return redirect('babyproducts:view_cart')
