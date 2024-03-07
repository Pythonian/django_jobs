from django.core.management.base import BaseCommand

from faker import Faker

from ...models import Testimonial

fake = Faker()


class Command(BaseCommand):
    help = "Populate the database with sample data for Testimonial"

    def handle(self, *args, **kwargs):
        for _ in range(5):
            Testimonial.objects.create(
                fullname=fake.name(),
                content=fake.text(),
                rating=fake.random_int(min=1, max=5),
            )
        self.stdout.write(self.style.SUCCESS("Successfully generated 5 Testimonials"))
