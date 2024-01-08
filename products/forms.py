from django import forms
from .models import Product

# Дописать permission
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
