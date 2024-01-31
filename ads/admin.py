from django.contrib import admin
from django.http import HttpRequest
from .models import Ads


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    # Конфигурация административной панели для модели Ads

    # Переопределение метода, чтобы разрешить доступ только суперпользователю
    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_superuser
