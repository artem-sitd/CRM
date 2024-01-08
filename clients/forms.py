from django import forms
from .models import Client


# Дописать permission
class ClientsForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
