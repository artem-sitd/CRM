from django import forms
from .models import Ads

# Дописать permission
class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = '__all__'
