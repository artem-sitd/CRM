from django.db import models


# Услуги
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)  # Цена услуги
    archived = models.BooleanField(default=False)
    description = models.CharField(max_length=500, null=True, blank=False, db_index=True)  # Описание услуги
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания