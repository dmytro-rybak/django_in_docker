import random
from django.core.management.base import BaseCommand
from custom_apps.person.models import Person
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker(locale='uk_UA')
        for _ in range(50):
            person = Person(first_name=fake.first_name(),
                            last_name=fake.last_name(),
                            age=random.randint(18, 60),
                            email=fake.email())
            person.save()
