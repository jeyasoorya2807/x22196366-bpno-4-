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
    
def add_to_cart(request id):
    product = get_object_or_404(Product, pk=id)
    return redirect('babyproducts:cart')

@login_required
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please log in to add items to your cart.')
        return redirect('users:sign_in')

    product = Babyproduct.objects.get(pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('babyproducts:view_cart')

@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if cart_items:
        order = Order.objects.create(user=request.user)
        order.items.set(cart_items)

        messages.success(request, "Your order has been placed. We are waiting for your arrival on the store.")

        # Clear the user's cart
        cart_items.delete()

    return redirect('babyproducts:product_list')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'babyproducts/cart.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, f"{cart_item.product.name} has been removed from your cart.")
    return redirect('babyproducts:view_cart')
