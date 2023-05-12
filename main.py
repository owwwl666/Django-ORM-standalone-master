import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402
from django.utils import timezone
from datetime import timedelta

if __name__ == '__main__':
    # Программируем здесь
    passcards = Passcard.objects.get(owner_name='Jennifer Martin')
    visits = Visit.objects

    # print(f'owner_name: {passcards[0].owner_name} \n'
    #       f'passcode: {passcards[0].passcode} \n'
    #       f'created_at: {passcards[0].created_at} \n'
    #       f'is_active: {passcards[0].is_active}')

    # for data in passcard:
    #     print(data.owner_name)

    # print(f'Количество пропусков: {passcards.count()} \n'
    #       f'Активных пропусков: {passcards.filter(is_active=True).count()}')

    moscow_time = timezone.localtime(timezone.now())
    visit_longer_10, visit_longer_1000 = [], []

    # for visit in visits:
    #     delta = moscow_time - visit.entered_at if not visit.leaved_at \
    #         else visit.leaved_at - visit.entered_at
    #     # print(f'Зашел в хранилище, время по Москве: {visit.entered_at} \n'
    #     #       f'Находится в хранилище:{delta + timedelta(hours=3)} \n')
    #     if delta > timedelta(minutes=60):
    #         print(visit)
    #
    # print(moscow_time)
    # print(f'Дольше 10 минут {visit_longer_10} \n'
    #       f'Дольше 1000 минут {visit_longer_1000}')

    print(visits.filter(passcard=passcards))
