from django.core.management.base import BaseCommand
from django.utils.text import slugify

from ...models import Category

categories = [
    "Account Management",
    "Job Search and Applications",
    "Recruitment Guide",
    "Technical Support",
    "Privacy and Security",
    "User Experience",
]

icons = [
    "user",
    "cog",
    "file",
    "question",
    "lock",
    "chart-bar",
]

descriptions = [
    "Manage your account settings and security.",
    "How to find and apply for jobs easily.",
    "Guidance for recruiters and job posters.",
    "Get technical assistance and troubleshooting tips.",
    "Learn about our privacy measures and security policies.",
    "Enhance your user experience with our platform.",
]


class Command(BaseCommand):
    help = "Populate the database with Help Categories data"

    def handle(self, *args, **kwargs):
        for i in range(len(categories)):
            Category.objects.get_or_create(
                name=categories[i],
                slug=slugify(categories[i]),
                description=descriptions[i],
                icon=icons[i],
            )
        self.stdout.write(self.style.SUCCESS(f"Successfully added {len(categories)} Help Categories"))
