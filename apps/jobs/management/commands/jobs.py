from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
import random
from ...models import Job, Category, JobType, State
from apps.accounts.models import Company, Employee

fake = Faker()


class Command(BaseCommand):
    help = 'Populate the database with sample data for the Job model'

    def handle(self, *args, **kwargs):
        companies = Company.objects.all()
        jobtypes = JobType.objects.all()
        states = State.objects.all()
        categories = Category.objects.all()

        for _ in range(50):
            title = fake.unique.job()
            slug = slugify(title)
            description = fake.text()
            salary_mode = random.choice(Job.SalarySchedule.choices)[0]
            base_salary_amount = fake.random_int(min=5000, max=100000, step=1000)
            maximum_salary_amount = fake.random_int(min=100000, max=200000, step=1000)
            experience = fake.random_int(min=1, max=5)
            vacancy = fake.random_int(min=1, max=20)
            application_deadline = fake.date_between(start_date='today', end_date='+1y')
            qualification_title = fake.job()
            gender = random.choice(Job.GenderStatus.choices)[0]
            status = random.choice(Job.JobStatus.choices)[0]
            category = random.choice(categories)
            jobtype = random.choice(jobtypes)
            company = random.choice(companies)
            address = fake.address()
            state = random.choice(states)
            impressions = fake.random_int(min=1, max=1000)
            sponsored = fake.boolean()
            created = fake.date_this_year()

            Job.objects.create(
                title=title,
                slug=slug,
                description=description,
                salary_mode=salary_mode,
                base_salary_amount=base_salary_amount,
                maximum_salary_amount=maximum_salary_amount,
                experience=experience,
                vacancy=vacancy,
                application_deadline=application_deadline,
                qualification_title=qualification_title,
                gender=gender,
                status=status,
                category=category,
                jobtype=jobtype,
                company=company,
                address=address,
                state=state,
                impressions=impressions,
                sponsored=sponsored,
                created=created
            )
