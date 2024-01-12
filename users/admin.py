from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import Group, User

admin.site.register(Profile)
admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    # Конфигурация административной панели для модели Ads

    # Переопределение метода, чтобы разрешить доступ только суперпользователю
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Конфигурация административной панели для модели Ads

    # Переопределение метода, чтобы разрешить доступ только суперпользователю
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
