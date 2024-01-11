from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Замените 'your_permission_codename' и 'Your Permission Name' на свои значения
        permission = Permission.objects.create(
            codename="view_ads_stat",
            name="Can view ads statistic",
            content_type=ContentType.objects.get_for_model(
                Group
            ),  # Можете заменить на ContentType другой модели
        )
