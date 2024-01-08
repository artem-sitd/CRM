from django import forms
from .models import Ads
from products.models import Product


# Дописать permission
class AdsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdsForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(archived=False)

    class Meta:
        model = Ads
        fields = ['title', 'price', 'archived', 'description', 'product', 'promotion']
