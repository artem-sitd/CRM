from django.contrib.auth.models import Group, Permission, User
from django.core.management import BaseCommand
from django.contrib.contenttypes.models import ContentType
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
        new_groups = ("Admins", "Operators", "Marketers", "Managers")
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

        for k, v in list(zip(new_groups, users_data)):
            get_user = User.objects.get(username=v["username"])
            get_group = Group.objects.get(name=k)
            add_groups(user1=get_user, group=get_group)

        """
            Ниже скрипт выполняет добавление permissions группам. 
            Можно было через словарь или еще как то упростить, но я решил пойти по длинному пути
        """

        operators_gr = Group.objects.get(name="Operators")
        marketer_gr = Group.objects.get(name="Marketers")
        manager_gr = Group.objects.get(name="Managers")
        admins_gr = Group.objects.get(name="Admins")

        permissions_operators = [
            "Can add client",
            "Can change client",
            "Can view client",
            "Can view ads statistic",
        ]
        operator_perm_id = []

        permissions_marketer = [
            "Can add product",
            "Can change product",
            "Can view product",
            "Can add ads",
            "Can change ads",
            "Can view ads",
            "Can view ads statistic",
        ]
        marketer_perm_id = []

        permissions_manager = [
            "Can add contract",
            "Can change contract",
            "Can view contract",
            "Can add client",
            "Can change client",
            "Can view client",
            "Can view ads statistic",
        ]
        manager_perm_id = []

        # Создание Специального разрешение для просмотра статистики рекламы
        permission = Permission.objects.create(
            codename="view_ads_stat",
            name="Can view ads statistic",
            content_type=ContentType.objects.get_for_model(Group),
        )

        permissions_admins = [
            "Can view ads",
            "Can view ads statistic",
            "Can view client",
            "Can view content type",
            "Can view contract",
            "Can view group",
            "Can view history ads",
            "Can view log entry",
            "Can view permission",
            "Can view product",
            "Can view profile",
            "Can view session",
            "Can view user",
        ]

        admins_perm_id = []

        # Добавление прав группе операторов
        for i in permissions_operators:
            operator_perm_id.append(Permission.objects.get(name=i).pk)
        operators_gr.permissions.set(operator_perm_id)
        self.stdout.write(
            self.style.SUCCESS(
                f"Для группы: {operators_gr} добавлены разрешения: {permissions_operators}"
            )
        )

        # Добавление прав группе маректологов
        for i in permissions_marketer:
            marketer_perm_id.append(Permission.objects.get(name=i).pk)
        marketer_gr.permissions.set(marketer_perm_id)
        self.stdout.write(
            self.style.SUCCESS(
                f"Для группы: {marketer_gr} добавлены разрешения: {permissions_marketer}"
            )
        )

        # Добавление прав группе менеджеров
        for i in permissions_manager:
            manager_perm_id.append(Permission.objects.get(name=i).pk)
        manager_gr.permissions.set(manager_perm_id)
        self.stdout.write(
            self.style.SUCCESS(
                f"Для группы: {manager_gr} добавлены разрешения: {permissions_manager}"
            )
        )

        # Добавление прав группе админов
        for i in permissions_admins:
            admins_perm_id.append(Permission.objects.get(name=i).pk)
        admins_gr.permissions.set(admins_perm_id)
        self.stdout.write(
            self.style.SUCCESS(
                f"Для группы: {admins_gr} добавлены разрешения: {permissions_admins}"
            )
        )

        self.stdout.write(f">>>>>>>")
        self.stdout.write(self.style.SUCCESS(f"Все команды выполнены"))
