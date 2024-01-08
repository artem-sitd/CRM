from django.core.management import BaseCommand
from users.models import Profile
from django.contrib.auth.models import User, Group
from products.models import Product

# Создание групп для сотрудников
class Command(BaseCommand):
    def handle(self, *args, **options):
        pro=Product.objects.filter(archived=False).order_by('id')
        print(pro)