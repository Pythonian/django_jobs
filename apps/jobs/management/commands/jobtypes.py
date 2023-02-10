from django.core.management.base import BaseCommand
from django.utils.text import slugify

from faker import Faker
from faker.providers import DynamicProvider

from ...models import JobType

elements = [
    "Internship",
    "Full-time",
    "Part-time",
    "Freelance",
    "Volunteer"
]

jobtypes_provider = DynamicProvider(
    provider_name="jobtypes",
    elements=elements,
)

fake = Faker()
fake.add_provider(jobtypes_provider)


class Command(BaseCommand):
    help = 'Populates the database with Job Types'

    def handle(self, *args, **kwargs):
        for _ in range(len(elements)):
            JobType.objects.get_or_create(
                name=fake.jobtypes(),
                slug=slugify(fake.jobtypes())
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully added {len(elements)} Job types'))
