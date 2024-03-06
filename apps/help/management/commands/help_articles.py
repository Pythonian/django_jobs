from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
import random

from ...models import Article, Category

fake = Faker()


class Command(BaseCommand):
    help = "Populate the database with sample data for Help Articles model"

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        for _ in range(50):
            title = fake.sentence(nb_words=5)
            slug = slugify(title)
            content = fake.paragraph(nb_sentences=10)
            category = random.choice(categories)

            Article.objects.create(
                title=title,
                slug=slug,
                content=content,
                category=category,
            )
        self.stdout.write(self.style.SUCCESS("Successfully added 50 Help Articles"))
