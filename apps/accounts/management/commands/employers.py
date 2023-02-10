from django.core.management.base import BaseCommand
# from django.conf import settings
# from django.contrib.auth.models import User
from django.utils.text import slugify
from faker import Faker

from apps.accounts.models import User
from ...models import Company

# User = settings.AUTH_USER_MODEL


class Command(BaseCommand):
    help = 'Create fake Companies'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of Companies to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        # existing_names = set(Company.objects.values_list('name', flat=True))
        # existing_slugs = set(Company.objects.values_list('slug', flat=True))

        for _ in range(total):
            # name = fake.company()
            # while name in existing_names:
            #     name = fake.unique.company()
            # existing_names.add(name)

            # slug = fake.slug()
            # while slug in existing_slugs:
            #     slug = fake.slug()
            # existing_slugs.add(slug)

            user = User.objects.get_or_create(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
                email_verified=True,
                is_company=True
            )
        # for i in range(total):
        #     # create a user
        #     user = User.objects.create(
        #         username=fake.user_name(),
        #         password=fake.password(),
        #         email_verified=True,
        #         is_company=True
        #     )
        #     user.save()

            # create a company
            company = Company.objects.get_or_create(
                user=user,
                name=fake.unique.company(),
                # name=name,
                # slug=slug,
                slug=slugify(fake.unique.company()),
                about=fake.text(max_nb_chars=5000),
                logo='img/avatar.svg',
                contact_person=fake.unique.name(),
                position_in_company=fake.job(),
                established=fake.date_between(start_date='-30y', end_date='today'),
                website=fake.url(),
                address=fake.address(),
                staff_strength=fake.random_element(
                    elements=Company.StaffStrength.choices)[0],
                phone_number=fake.phone_number(),
            )
            # company.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} companies.'))
