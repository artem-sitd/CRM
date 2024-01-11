from django.core.management import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from clients.models import HistoryAds, Client

from contracts.models import Contract

"""
●	Администратор может создавать, просматривать и редактировать пользователей, назначать им роли и разрешения. 
Такой функционал реализует административная панель Django.

●	Оператор может создавать, просматривать и редактировать потенциальных клиентов.

●	Маркетолог может создавать, просматривать и редактировать предоставляемые услуги и рекламные кампании.

●	Менеджер может создавать, просматривать и редактировать контракты, смотреть потенциальных клиентов и 
переводить их в активных.

●	Все роли могут смотреть статистику рекламных кампаний.

    group.permissions.set([permission_list])
"""


# Создание групп для сотрудников
class Command(BaseCommand):
    def handle(self, *args, **options):
        ads_hs = HistoryAds.objects.all().values_list('id', flat=True)
        for i in ads_hs:
            contracts = Contract.objects.filter(archived=False,
                                             ads_history__id=i).only('id').exists()
            if contracts:
                target = HistoryAds.objects.get(id=i).client.id
                cl = Client.objects.get(id=target)
                cl.state = 'Active'
                cl.save()
                print(cl.state)
