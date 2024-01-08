"""
Клиент - имеет свое состояние: Потенциальный, активный (действующий контракт), не активный (контракты закончились)
"""
from django.db import models
from ads.models import Ads
from contracts.models import Contract


class Client(models.Model):
    name = models.CharField(max_length=40, blank=False, null=True, default='введите в это поле имя')  # Имя
    second_name = models.CharField(max_length=50, blank=False, null=True, default='введите в это поле фамилию')  # Фамилия
    surname = models.CharField(max_length=50, blank=True, null=True, default='введите в это поле отчество')  # Отчество
    phone = models.CharField(max_length=12, blank=False, null=True, default="+0123456789")  # Телефон
    email = models.EmailField(max_length=50, default="example@mail.com", blank=True, null=True)  # Почта
    ads = models.ForeignKey(Ads, on_delete=models.SET_NULL,
                            null=True)  # Модель рекламы (ads) раскомментировать после создания модели рекламы
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    STATE_CHOICES = [
        ('POTENTIAL', 'Потенциальный'),
        ('ACTIVE', 'Активный'),
        ('INACTIVE', 'Неактивный'),
    ]
    state = models.CharField(choices=STATE_CHOICES, max_length=20, default='POTENTIAL')
    contract = models.OneToOneField(Contract, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'ФИО: {self.name} {self.second_name} {self.surname}, телефон: {self.phone}'
