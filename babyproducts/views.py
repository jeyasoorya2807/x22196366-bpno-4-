import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Babyproduct, CartItem, Order
from .forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required
import json 

endpoint = "https://2arbn3zs3e.execute-api.eu-west-1.amazonaws.com/dev"

# Function to fetch Instagram API data
def fetch_instagram_data():
    url = "https://v1.nocodeapi.com/jeyasooryamanoharan/instagram/GKvklxfApuGJuqdU"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

parenting_tips_api_url = "https://tggng1eo47.execute-api.eu-west-1.amazonaws.com/default/x22196366-parentingtips"
name_meaning_api_url = "https://9gzuemu06f.execute-api.eu-west-1.amazonaws.com/development"

def get_parenting_tip():
    """
    Get a parenting tip from the Lambda function.
    """
    try:
        response = requests.get(parenting_tips_api_url)
        response.raise_for_status()  # Raise an error for non-200 status codes
        return response.json().get('parenting_tip', '')
    except requests.RequestException as e:
        # Handle API request errors
        return ""

@login_required
def index(request):
    name = request.GET.get('name', '')  # Get the 'name' parameter from the query string
 
    if request.method == 'POST':
        # If the request method is POST, meaning the form has been submitted
        name = request.POST.get('name', '')  # Get the name from the form data
 
    name_meaning = {}
 
    if name:
        try:
            # Example API call to retrieve data from the Lambda function
            payload = {'name': name}
            headers = {'Content-Type': 'application/json'}
 
            response = requests.post(name_meaning_api_url, data=json.dumps(payload), headers=headers)
            response.raise_for_status()  # Raise an error for non-200 status codes
 
            name_meaning = response.json().get('body', {})
            print('name_meaning:', name_meaning)
        except requests.RequestException as e:
            # Handle API request errors
            name_meaning = {'error': 'Failed to fetch name meaning'}

    parenting_tip = get_parenting_tip()
 
    return render(request, 'babyproducts/index.html', {'name_meaning': name_meaning, 'parenting_tip': parenting_tip})

@login_required
def product_list(request):
    products = Babyproduct.objects.all()
    # Fetch reviews for each product and add them to the product objects
    for product in products:
        product.reviews = get_reviews_from_api(product.id)  # Assuming get_reviews_from_api retrieves reviews for a given product ID

    return render(request, 'babyproducts/products_list.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('babyproducts:product_list')
    else:
        form = ProductForm()
    return render(request, 'babyproducts/add_product.html', {'form': form})

@login_required
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please log in to add items to your cart.')
        return redirect('sign_in')

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
    # Sample Instagram data for testing
    instagram_data =[
        {
            "media_url": "https://scontent.cdninstagram.com/v/t51.29350-15/439022523_1106114107311452_6796697862091274425_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=18de74&_nc_ohc=9IJxU9lDRx0Ab43pj7b&_nc_ht=scontent.cdninstagram.com&edm=ANo9K5cEAAAA&oh=00_AfAussIqOoG1IBAtD9otDwVnlrf4xeAtYI7Mpk9b3ftDEg&oe=6625F867",
            "permalink": "https://www.instagram.com/x22196366_baby_products",
            "username": "x22196366_baby_products",
            "timestamp": "2023-12-17T20:54:10+0000"
        }
    ]
    return render(request, 'babyproducts/cart.html', {'cart_items': cart_items, 'instagram_posts': instagram_data})

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, f"{cart_item.product.name} has been removed from your cart.")
    return redirect('babyproducts:view_cart')

@login_required
def add_review(request, product_id):
    babyproduct = get_object_or_404(Babyproduct, pk=product_id)
   
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
           
            user_id = request.user.username
            submit_review_to_api(request, user_id, product_id, content)
           
            # Redirect the user back to the product detail page
            return redirect('babyproducts:product_list')
    else:
        # If the request method is not POST, render the form
        form = ReviewForm()
   
    # Render the add review form template
    return render(request, 'babyproducts/index.html', {'form': form, 'babyproduct': babyproduct})

def submit_review_to_api(request, user_id, product_id, content):
    # Call the API endpoint to submit a new review
    data = {'application': 'babyproducts', 'rid': product_id, 'user_id': user_id, 'content': content}
    response = requests.post(endpoint, json=data)
 
    if response.status_code == 200:
        messages.success(request, "Review created successfully")
    else:
        # Handle error response if needed
        messages.error(request, "Failed to create review")
 
def get_reviews_from_api(product_id):
    response = requests.get(endpoint, params={'application': 'babyproducts','rid': product_id})
 
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return []  # Return empty list if no reviews found or error occurred
        


