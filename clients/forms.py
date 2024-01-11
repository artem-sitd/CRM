from django import forms
from django.contrib import messages
from contracts.models import Contract
from .models import Client, HistoryAds


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
    to_inactive = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput)
    to_potential = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput)

    class Meta(ClientsForm.Meta):
        exclude = ['state']  # Исключаем state из формы
        widgets = {'phone': forms.HiddenInput(attrs={'readonly': 'readonly'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Получаем текущий state пользователя
        current_state = self.instance.state if self.instance and hasattr(self.instance, 'state') else None

        # В зависимости от текущего state скрываем или показываем соответствующий чекбокс
        if current_state == 'Active':
            self.fields['to_inactive'].widget = forms.HiddenInput()
            self.fields['to_potential'].widget = forms.HiddenInput()

        elif current_state == 'POTENTIAL':
            self.fields['to_potential'].widget = forms.HiddenInput()
            self.fields['to_inactive'].label = "Перевести в состояние INACTIVE"

        elif current_state == 'INACTIVE':
            self.fields['to_inactive'].widget = forms.HiddenInput()
            self.fields['to_potential'].label = "Перевести в состояние POTENTIAL"

    def clean(self):
        cleaned_data = super().clean()
        to_inactive = cleaned_data.get('to_inactive')

        # Данная проверка скорее всего не будет происходить, т.к. в форме будет отсутствовать чекбокс
        # перевода если состояние клиента Active
        if to_inactive:
            ads_hs = HistoryAds.objects.filter(client=self.instance.id).values_list('id', flat=True)
            contracts_exist = Contract.objects.filter(archived=False, ads_history__id__in=ads_hs).exists()

            if contracts_exist:
                messages.warning(self.request,
                                 "Невозможно перевести в состояние INACTIVE. У клиента есть активные контракты.")
                self.add_error('to_inactive',
                               'Невозможно перевести в состояние INACTIVE. У клиента есть активные контракты.')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get('to_inactive'):
            instance.state = 'INACTIVE'

        elif self.cleaned_data.get('to_potential') and instance.state == 'INACTIVE':
            instance.state = 'POTENTIAL'

        if commit:
            instance.save()

        return instance
