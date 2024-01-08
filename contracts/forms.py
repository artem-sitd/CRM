from django import forms
from .models import Contract
from products.models import Product


class ContractsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContractsForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(archived=False)

    class Meta:
        model = Contract
        fields = '__all__'
        widgets = {'validity': forms.DateTimeInput(attrs={'type': 'date'})}
