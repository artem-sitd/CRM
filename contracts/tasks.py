import sys
from .models import Contract
from django.utils import timezone
from celery import shared_task


# @shared_task
# def test5sec():
#     sys.stdout.write('task 5 sec')
#     print('task 5 sec')
#
#
# @shared_task
# def test10sec():
#     sys.stdout.write('task 10 sec')
#     print('task 10 sec')

@shared_task
def check_validity_contracts():
    active_contracts = Contract.objects.filter(archived=False).only('validity')
    for contract in active_contracts:
        if contract.validity <= timezone.now():
            contract.archived = True
            contract.save()
            print('Актуальность контрактов проверена')
