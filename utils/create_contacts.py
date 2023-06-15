import os
import sys
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import contact

    fake = faker.Faker('pt_BR')

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        description = fake.text(max_nb_chars=100)
        city = fake.address()

        django_contacts.append(
            contact(
                first_name=first_name,
                last_name=last_name,
                city=city,
                phone=phone,
                email=email,
                description=description,
            )
        )

    if len(django_contacts) > 0:
        contact.objects.bulk_create(django_contacts)