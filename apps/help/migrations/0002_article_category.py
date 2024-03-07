# Generated by Django 5.0.2 on 2024-02-25 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("help", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                default=1,
                help_text="Category linked to this Help Article.",
                on_delete=django.db.models.deletion.PROTECT,
                to="help.category",
                verbose_name="category",
            ),
            preserve_default=False,
        ),
    ]