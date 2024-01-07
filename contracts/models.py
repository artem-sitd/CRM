from django.db import models
from products.models import Product


class Contract(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)  # Сумма
    archived = models.BooleanField(default=False)
    description = models.CharField(max_length=500, null=True, blank=False, db_index=True)  # Описание рекламы
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)  # раскомментировать после создания услуг
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    validity = models.DateTimeField(blank=False, null=True)  # Дата окончания
    file = models.FileField(null=True, upload_to='contracts/file')  # Договор, или другой файл
