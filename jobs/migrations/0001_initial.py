# Generated by Django 4.1.1 on 2022-10-06 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jobs.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=25, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, upload_to=jobs.utils.image_path, verbose_name='Image')),
                ('category_order', models.PositiveIntegerField(blank=True, unique=True, verbose_name='Category order')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['category_order'],
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=15, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Job Type',
                'verbose_name_plural': 'Job Types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=25, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('salary_mode', models.CharField(choices=[('H', 'Hourly'), ('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')], max_length=1, verbose_name='Salary Mode')),
                ('salary_amount', models.PositiveIntegerField()),
                ('experience', models.PositiveIntegerField(blank=True, null=True, verbose_name='Years of experience')),
                ('vacancy', models.PositiveIntegerField(blank=True, null=True)),
                ('application_deadline', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=1)),
                ('impressions', models.PositiveIntegerField(default=0)),
                ('sponsored', models.BooleanField(default=False, verbose_name='Sponsored')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.category', verbose_name='Category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL, verbose_name='Company')),
                ('jobtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.jobtype', verbose_name='Job Type')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.state', verbose_name='State')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
                'ordering': ['-created'],
            },
        ),
    ]
