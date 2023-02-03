from django.core.management.base import BaseCommand
from django.utils.text import slugify
from ...models import State
import json

class Command(BaseCommand):
    # python manage.py states fixtures/states.json
    help = 'Populates the database with States in Nigeria'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='States to be added to the database')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            data = json.load(file)
            for state in data['states']:
                state, created = State.objects.get_or_create(name=state, slug=slugify(state))
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Successfully added {state} to the database"))
                else:
                    self.stdout.write(self.style.WARNING(f"{state} already exists in the database"))

        self.stdout.write(self.style.SUCCESS(f'The states have been successfully populated.'))
