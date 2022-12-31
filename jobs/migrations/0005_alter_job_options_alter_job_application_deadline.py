# Generated by Django 4.1.1 on 2022-10-10 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_job_maximum_salary_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['application_deadline', '-created'], 'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
        migrations.AlterField(
            model_name='job',
            name='application_deadline',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]