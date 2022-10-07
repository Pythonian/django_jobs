# Generated by Django 4.1.1 on 2022-10-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_location_company_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_email',
        ),
        migrations.AddField(
            model_name='company',
            name='contact_person',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Company name'),
        ),
    ]
