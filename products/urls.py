"""
URL's модели услуг. 1 Создание, 2 удаление, 3 детальная страница, 4 редактирование, 5 полный список
"""
from django.urls import path

from .views import (DeleteProduct, DetailProduct, ListProducts,
                    ProductUpdateView, create_product)

app_name = "products"
# Услуги
urlpatterns = [
    path("create/", create_product, name="products-create"),
    path("<int:pk>/delete/", DeleteProduct.as_view(), name="products-delete"),
    path("detail/<int:pk>/", DetailProduct.as_view(), name="products-detail"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="products-edit"),
    path("list/", ListProducts.as_view(), name="products-list"),
]
