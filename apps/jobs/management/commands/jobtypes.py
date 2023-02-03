from django.core.management.base import BaseCommand
from django.utils.text import slugify
from ...models import JobType


class Command(BaseCommand):
    # python manage.py jobtypes Lagos Ogun Oyo
    help = 'Populates the database with Job Types'

    def add_arguments(self, parser):
        parser.add_argument('jobtypes', type=str, nargs='+', help='Job Types to be added to the database')

    def handle(self, *args, **kwargs):
        jobtypes = kwargs['jobtypes']

        for jobtype in jobtypes:
            JobType.objects.get_or_create(name=jobtype, slug=slugify(jobtype))
        self.stdout.write(self.style.SUCCESS(f'Successfully added {len(jobtype)} Job types'))
