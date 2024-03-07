from django.core.management.base import BaseCommand

from faker import Faker

from ...models import FrequentlyAskedQuestion

fake = Faker()


class Command(BaseCommand):
    help = "Populate the database with sample data for FrequentlyAskedQuestion"

    def handle(self, *args, **kwargs):
        for _ in range(8):
            FrequentlyAskedQuestion.objects.create(
                question=fake.text(),
                answer=fake.paragraph(nb_sentences=10),
            )
        self.stdout.write(self.style.SUCCESS("Successfully generated 8 FAQs"))
