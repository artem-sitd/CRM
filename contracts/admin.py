from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractsAdmin(admin.ModelAdmin):
    # Конфигурация административной панели для модели Ads

    # Переопределение метода, чтобы разрешить доступ только суперпользователю
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
