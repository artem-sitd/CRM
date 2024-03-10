import uuid

from django.db import models

from clients.models import HistoryAds
from products.models import Product


def contract_file(instance: "Contract", filename) -> str:
    return "contracts/contract_{uniq_id}/{filename}".format(
        uniq_id=instance.uniq_id, filename=filename
    )


class Contract(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)  # Сумма
    archived = models.BooleanField(default=False)
    description = models.CharField(
        max_length=500, null=True, blank=False, db_index=True
    )  # Описание рекламы
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True
    )  # раскомментировать после создания услуг
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    validity = models.DateTimeField(blank=False, null=True)  # Дата окончания
    file = models.FileField(
        null=True, upload_to=contract_file, blank=True
    )  # Договор, или другой файл
    ads_history = models.ForeignKey(HistoryAds, on_delete=models.SET_NULL, null=True)

    # ДАННОЕ ПОЛЕ ИСПОЛЬЗУЕТСЯ ТОЛЬКО ДЛЯ КОРРЕКТНОЙ ГЕНЕРАЦИИ НОМЕРА ПАПКИ ПРИ СОХРАНЕНИИ ФАЙЛА, Т.К.
    # ПРИ ИСОПЛЬЗОВАНИИ ФУНКЦИИ contract_file У INSTANCE ОБЪЕКТА ЕЩЕ НЕТ ПЕРВИЧНОГО КЛЮЧА И ПОЛУЧАЕТСЯ ПАПКА CONTRACT_NONE
    uniq_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def formatted_created_at(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def formatted_validity(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.title}. {self.price}"
