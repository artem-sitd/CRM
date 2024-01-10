from django import forms
from .models import Client


# Дописать permission
class ClientsForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


# Дописать permission. Проверка наличия такого номера в базе
class CheckPhoneForm(ClientsForm):
    class Meta(ClientsForm.Meta):
        fields = ['phone']

# Дописать permission
class LeadUpdateForm(ClientsForm):
    class Meta(ClientsForm.Meta):
        widgets = {
            'phone': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
