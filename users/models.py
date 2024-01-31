"""
1. Администратор может создавать, просматривать и редактировать пользователей, назначать им роли
    и разрешения. Такой функционал реализует административная панель Django.
2. Оператор может создавать, просматривать и редактировать потенциальных клиентов.
3. Маркетолог может создавать, просматривать и редактировать предоставляемые услуги и рекламные кампании.
4. Менеджер может создавать, просматривать и редактировать контракты, смотреть потенциальных клиентов и переводить их в активных.
* Все роли могут смотреть статистику рекламных кампаний.
"""
from django.contrib.auth.models import User
from django.db import models


# Профиль для сотрудников
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=False, null=True)  # Имя
    second_name = models.CharField(max_length=50, blank=False, null=True)  # Фамилия
    surname = models.CharField(max_length=40, blank=True, null=True)  # Отчество
    fired = models.BooleanField(
        default=False, null=True, blank=True
    )  # Для сотрудников. Если True - уволен
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    phone = models.CharField(
        max_length=12, blank=False, null=True, default="+0123456789"
    )  # Телефон
    email = models.EmailField(
        max_length=50, default="example@mail.com", blank=True, null=True
    )  # Почта

    # Можно еще придумать поля адресов(страна, город, улица и прочее)

    def __str__(self: "object of class Client") -> str:
        return (
            f"Имя: {self.name}, Фамилия: {self.second_name}, Отчество: {self.surname}"
        )
