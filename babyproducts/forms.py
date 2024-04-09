from django import forms
from .models import Babyproduct
 
class ProductForm(forms.ModelForm):
    class Meta:
        model = Babyproduct
        fields = ['name', 'description', 'price', 'image'] 

class ReviewForm(forms.Form):
    content = forms.CharField(label='Your Review', widget=forms.Textarea)