from django.contrib.auth.models import Group, Permission, User
from django.core.management import BaseCommand

from users.models import Profile

"""
●	Администратор может создавать, просматривать и редактировать пользователей, назначать им роли и разрешения. Такой функционал реализует административная панель Django.
●	Оператор может создавать, просматривать и редактировать потенциальных клиентов.
●	Маркетолог может создавать, просматривать и редактировать предоставляемые услуги и рекламные кампании.
●	Менеджер может создавать, просматривать и редактировать контракты, смотреть потенциальных клиентов и переводить их в активных.
●	Все роли могут смотреть статистику рекламных кампаний.
"""


# Создание групп для сотрудников
class Command(BaseCommand):
    def handle(self, *args, **options):
        # Создание групп
        new_groups = ("Operators", "Marketers", "Managers")
        for gr in new_groups:
            Group.objects.create(name=gr)
            self.stdout.write(self.style.SUCCESS(f"Создана группа: {gr}"))

        users_data = [
            {
                "username": "crm_admin1",
                "email": "admin@example.com",
                "password": "123",
                "is_staff": True,  # Администратор
                "second_name": "crm_admin1",
            },
            {
                "username": "operator",
                "email": "operator@example.com",
                "password": "123",
                "second_name": "operator",
                "surname": "operator",
            },
            {
                "username": "marketer",
                "email": "marketer@example.com",
                "password": "123",
                "second_name": "marketer",
                "surname": "marketer",
            },
            {
                "username": "manager",
                "email": "manager@example.com",
                "password": "123",
                "second_name": "manager",
                "surname": "manager",
            },
        ]

        # Create User objects and Profiles
        for data in users_data:
            user = User.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
                is_staff=data.get("is_staff", False),
            )
            self.stdout.write(
                self.style.SUCCESS(f'Создан пользователь: {data["username"]}')
            )

            profile = Profile.objects.create(
                user=user,
                name=data["username"],
                email=data.get("email"),
                second_name=data.get("second_name", "second_name"),
                surname=data.get("surname", "surname"),
            )
            profile.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'Создан профиль, для пользователя: {data["username"]}'
                )
            )

        # Добавление пользователей в группы
        def add_groups(user1=None, group=None):
            user1.groups.add(group)
            self.stdout.write(
                self.style.SUCCESS(f"Пользователь: {user1} добавлен в группу: {group}")
            )

        for k, v in list(zip(new_groups, users_data[1:])):
            get_user = User.objects.get(username=v["username"])
            get_group = Group.objects.get(name=k)
            add_groups(user1=get_user, group=get_group)

        # Добавление permissions группам

        operators_gr = Group.objects.get(name="Operators")
        marketer_gr = Group.objects.get(name="Marketers")
        manager_gr = Group.objects.get(name="Managers")

        permissions_operators = [
            "Can add client",
            "Can change client",
            "Can view client",
        ]
        operator_perm_id = []

        permissions_marketer = [
            "Can add product",
            "Can change product",
            "Can view product",
            "Can add ads",
            "Can change ads",
            "Can view ads",
        ]
        marketer_perm_id = []

        permissions_manager = [
            "Can add contract",
            "Can change contract",
            "Can view contract",
            "Can add client",
            "Can change client",
            "Can view client",
        ]
        manager_perm_id = []

        for i in permissions_operators:
            operator_perm_id.append(Permission.objects.get(name=i).pk)
        operators_gr.permissions.set(operator_perm_id)
        self.stdout.write(
            self.style.SUCCESS(
                f"Для группы: {operators_gr} добавлены разрешения: {permissions_operators}"
            )
        )

        for i in permissions_marketer:
            marketer_perm_id.append(Permission.objects.get(name=i).pk)
        marketer_gr.permissions.set(marketer_perm_id)
        self.stdout.write(
            self.style.SUCCESS(
                f"Для группы: {marketer_gr} добавлены разрешения: {permissions_marketer}"
            )
        )

        for i in permissions_manager:
            manager_perm_id.append(Permission.objects.get(name=i).pk)
        manager_gr.permissions.set(manager_perm_id)
        self.stdout.write(
            self.style.SUCCESS(
                f"Для группы: {manager_gr} добавлены разрешения: {permissions_manager}"
            )
        )

        self.stdout.write(f">>>>>>>")
        self.stdout.write(self.style.SUCCESS(f"Все команды выполнены"))
