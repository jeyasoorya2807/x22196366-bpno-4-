from django.urls import path
from . import views

app_name = 'babyproducts'

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.product_list, name='product_list'),
    path('', views.index, name='index'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
