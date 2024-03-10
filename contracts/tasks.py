from celery import shared_task
from django.utils import timezone

from .models import Contract


@shared_task
def check_validity_contracts():
    active_contracts = Contract.objects.filter(archived=False).only("validity")
    for contract in active_contracts:
        if contract.validity <= timezone.now():
            contract.archived = True
            contract.save()
            print("Актуальность контрактов проверена")
