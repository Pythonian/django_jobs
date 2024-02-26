from django.core.management.base import BaseCommand
from django.utils.text import slugify

from faker import Faker
from faker.providers import DynamicProvider

from ...models import Category

elements = [
    "Getting Started",
    "Your Account",
    "General Settings",
    "Technical Issues",
    "Favourite Pages",
    "Report Guidelines",
]

helpcategory_provider = DynamicProvider(
    provider_name="helpcategory",
    elements=elements,
)

fake = Faker()
fake.add_provider(helpcategory_provider)


class Command(BaseCommand):
    help = "Populate the database with Help Categories data"

    def handle(self, *args, **kwargs):
        for _ in range(len(elements)):
            Category.objects.get_or_create(
                name=fake.helpcategory(),
                slug=slugify(fake.helpcategory()),
                description=fake.text(),
                icon="user",
            )
        self.stdout.write(self.style.SUCCESS(f"Successfully added {len(elements)} Help Categories"))
