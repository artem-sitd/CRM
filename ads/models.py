from django.db import models

from products.models import Product


# Реклама
class Ads(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)  # Бюджет
    archived = models.BooleanField(default=False)
    description = models.CharField(
        max_length=500, null=True, blank=False, db_index=True
    )  # Описание рекламы
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    promotion_choice = (
        ("INSTAGRAM", "INSTAGRAM"),
        ("YOUTUBE", "YOUTUBE"),
        ("2GIS", "2GIS"),
        ("GOOGLE", "GOOGLE"),
        ("YANDEX", "YANDEX"),
        ("SITE", "SITE"),
        ("AVITO", "AVITO"),
        ("VK_GROUP", "VK_GROUP"),
        ("VK_ADS", "VK_ADS"),
        ("TG_CHANNEL", "TG_CHANNEL"),
        ("TG_ADS", "TG_ADS"),
        ("other", "other"),
    )
    promotion = models.CharField(choices=promotion_choice, blank=False, null=True)

    def __str__(self):
        return f"{self.title}, {self.product}, {self.promotion}"
