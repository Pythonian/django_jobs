# Generated by Django 4.1.1 on 2022-10-10 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='year',
            new_name='year_ended',
        ),
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='user',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='user',
        ),
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='account.resume'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='year_of_admission',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='company_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='resume',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='account.resume'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='year_started',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='city',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='country',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='first_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='last_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AddField(
            model_name='resume',
            name='professional_summary_or_objective',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='professional_title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='website',
            field=models.URLField(default='', verbose_name='Personal website or blog'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experience',
            name='job_title',
            field=models.CharField(max_length=50, verbose_name='Job title or Position'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='task_description',
            field=models.TextField(verbose_name='Achievements or Responsibilities'),
        ),
    ]
