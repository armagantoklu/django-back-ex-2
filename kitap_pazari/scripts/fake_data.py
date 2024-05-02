import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitap_pazari.settings')

import django

django.setup()

from django.contrib.auth.models import User
from faker import Faker
import requests

fake = Faker(['en_US'])


def set_user():
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    u_email = f'{u_name.lower()}@{fake.domain_name()}'
    print(f_name, l_name, u_name, u_email)

    user_check = User.objects.filter(username=u_name)

    while user_check.exists():
        u_name = u_name + str(random.randrange(1, 99))
        user_check = User.objects.filter(username=u_name)

    user = User(
        username=u_name,
        email=u_email,
        first_name=f_name,
        last_name=l_name,
        is_staff=fake.boolean(chance_of_getting_true=50),
    )
    user.set_password('root')
    user.save()


from kitaplar.api.serializers import KitapSerializer


def kitap_ara(konu):
    url = f'https://openlibrary.org/search.json'
    payload = {'q': konu}
    r = requests.get(url, params=payload)
    if r.status_code != 200:
        print(f'Konu error: {r.status_code}')
        return
    jsn = r.json()
    kitaplar = jsn.get('docs')
    for kitap in kitaplar:
        if kitap.get('title') and kitap.get('author_name'):
            data = dict(
                isim=kitap.get('title'),
                yazar=kitap.get('author_name')[0],
                aciklama='-'.join(kitap.get('author_name')),
                yayin_tarihi=fake.date_time_between(start_date='-10y', end_date='now', tzinfo=None),
            )
            serializer = KitapSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                continue
