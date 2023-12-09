from django import forms
from .models import Babyproduct
 
class ProductForm(forms.ModelForm):
    class Meta:
        model = Babyproduct
        fields = ['name', 'description', 'price', 'image'] 