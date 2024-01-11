from django import forms

from products.models import Product

from .models import Ads


class AdsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdsForm, self).__init__(*args, **kwargs)
        self.fields["product"].queryset = Product.objects.filter(archived=False)

    class Meta:
        model = Ads
        fields = ["title", "price", "archived", "description", "product", "promotion"]
