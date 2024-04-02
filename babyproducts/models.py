from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
 
class Babyproduct(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    weight = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    height = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')

 
    def __str__(self):
        return self.name

 
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Babyproduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
 
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    timestamp = models.DateTimeField(auto_now_add=True)