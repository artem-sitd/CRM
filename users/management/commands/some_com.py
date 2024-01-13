from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Замените 'your_permission_codename' и 'Your Permission Name' на свои значения
        # permission = Permission.objects.create(
        #     codename="view_ads_stat",
        #     name="Can view ads statistic",
        #     content_type=ContentType.objects.get_for_model(
        #         Group
        #     ),  # Можете заменить на ContentType другой модели
        # )

        crm_admin = User.objects.get(username='crm_admin1')
        permission_group = crm_admin.groups.all().first().permissions.all().order_by('name')
        for i in permission_group:
            print(i.name)

    permissions_admins = [
        'Can view ads',
        'Can view ads statistic',
        'Can view client',
        'Can view content type',
        'Can view contract',
        'Can view group',
        'Can view history ads',
        'Can view log entry',
        'Can view permission',
        'Can view product',
        'Can view profile',
        'Can view session',
        'Can view user'
    ]
