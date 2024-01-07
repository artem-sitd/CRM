from django.core.management import BaseCommand
from users.models import Profile
from django.contrib.auth.models import User, Group


# Создание групп для сотрудников
class Command(BaseCommand):
    def handle(self, *args, **options):
        # Создание групп
        new_groups = ('Operators', 'Marketers', 'Managers')
        for gr in new_groups:
            Group.objects.create(name=gr)

        users_data = [
            {
                'username': 'crm_admin1',
                'email': 'admin@example.com',
                'password': '123',
                'is_staff': True,  # Администратор
                'second_name': 'crm_admin1'
            },
            {
                'username': 'operator',
                'email': 'operator@example.com',
                'password': '123',
                'second_name': 'operator',
                'surname': 'operator'

            },
            {
                'username': 'marketer',
                'email': 'marketer@example.com',
                'password': '123',
                'second_name': 'marketer',
                'surname': 'marketer'
            },
            {
                'username': 'manager',
                'email': 'manager@example.com',
                'password': '123',
                'second_name': 'manager',
                'surname': 'manager'
            },
        ]

        # Create User objects and Profiles
        for data in users_data:
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                is_staff=data.get('is_staff', False),
            )
            profile = Profile.objects.create(
                user=user,
                name=data['username'],
                email=data.get('email'),
                second_name=data.get('second_name', 'second_name'),
                surname=data.get('surname', 'surname')
            )
            profile.save()

        # Добавление пользователей в группы
        def add_groups(user1=None, group=None):
            user1.groups.add(group)

        for k, v in list(zip(new_groups, users_data[1:])):
            get_user = User.objects.get(username=v['username'])
            get_group = Group.objects.get(name=k)
            add_groups(user1=get_user, group=get_group)
