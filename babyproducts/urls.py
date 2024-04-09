from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'babyproducts'

urlpatterns = [
    path('babyproducts/', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('product_list/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
