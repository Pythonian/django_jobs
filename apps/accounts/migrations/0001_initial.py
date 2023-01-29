# Generated by Django 4.1.5 on 2023-01-29 05:06

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="email address")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                ("is_company", models.BooleanField(default=False)),
                ("is_employee", models.BooleanField(default=False)),
                ("email_verified", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                ("gender", models.CharField(choices=[("M", "Male"), ("F", "Female")], max_length=1)),
                ("phone_number", models.CharField(blank=True, max_length=13)),
                ("location", models.CharField(max_length=50)),
                ("about", models.TextField()),
                ("image", models.ImageField(blank=True, upload_to="employees")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Resume",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("professional_title", models.CharField(max_length=50)),
                ("professional_summary_or_objective", models.TextField(max_length=1000)),
                ("city", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                ("phone_number", models.CharField(blank=True, max_length=13)),
                ("language_spoken", models.CharField(blank=True, max_length=200)),
                ("website", models.URLField(verbose_name="Personal website or blog")),
                ("company_name", models.CharField(max_length=50)),
                ("company_description", models.TextField(blank=True)),
                ("job_title", models.CharField(max_length=50, verbose_name="Job title or Position")),
                ("supervisor_name", models.CharField(blank=True, max_length=50, null=True)),
                ("supervisor_email", models.EmailField(blank=True, max_length=254, null=True)),
                ("task_description", models.TextField(verbose_name="Achievements or Responsibilities")),
                ("year_started", models.PositiveIntegerField()),
                ("year_ended", models.PositiveIntegerField()),
                ("location", models.CharField(max_length=50)),
                (
                    "education_level",
                    models.CharField(
                        choices=[
                            ("PS", "Primary School"),
                            ("SS", "Secondary School"),
                            ("VO", "Vocational School"),
                            ("CE", "College of Education"),
                            ("PO", "Polytechnic"),
                            ("UI", "University"),
                        ],
                        max_length=2,
                    ),
                ),
                ("name_of_institution", models.CharField(max_length=50)),
                ("year_of_admission", models.PositiveIntegerField()),
                ("year_of_graudation", models.PositiveIntegerField()),
                ("course_of_study", models.CharField(max_length=50)),
                ("employee", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="accounts.employee")),
            ],
            options={
                "ordering": ["professional_title"],
            },
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("company_name", models.CharField(max_length=50)),
                ("company_description", models.TextField(blank=True)),
                ("job_title", models.CharField(max_length=50, verbose_name="Job title or Position")),
                ("supervisor_name", models.CharField(blank=True, max_length=50, null=True)),
                ("supervisor_email", models.EmailField(blank=True, max_length=254, null=True)),
                ("task_description", models.TextField(verbose_name="Achievements or Responsibilities")),
                ("year_started", models.PositiveIntegerField()),
                ("year_ended", models.PositiveIntegerField()),
                ("location", models.CharField(max_length=50)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "resume",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name="experiences", to="accounts.resume"
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "education_level",
                    models.CharField(
                        choices=[
                            ("PS", "Primary School"),
                            ("SS", "Secondary School"),
                            ("VO", "Vocational School"),
                            ("CE", "College of Education"),
                            ("PO", "Polytechnic"),
                            ("UI", "University"),
                        ],
                        max_length=2,
                    ),
                ),
                ("name_of_institution", models.CharField(max_length=50)),
                ("year_of_admission", models.PositiveIntegerField()),
                ("year_of_graudation", models.PositiveIntegerField()),
                ("course_of_study", models.CharField(max_length=50)),
                (
                    "resume",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="education", to="accounts.resume"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Company name")),
                ("slug", models.SlugField(max_length=100, null=True, unique=True)),
                ("about", models.TextField(max_length=5000)),
                ("logo", models.ImageField(blank=True, default="img/avatar.svg", upload_to="logos")),
                ("contact_person", models.CharField(max_length=255)),
                ("position_in_company", models.CharField(max_length=50)),
                ("established", models.DateField(blank=True, null=True)),
                ("website", models.URLField(blank=True, null=True)),
                ("address", models.CharField(blank=True, max_length=50)),
                (
                    "staff_strength",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("SIZE_1_9", "1-9"),
                            ("SIZE_10_49", "10-49"),
                            ("SIZE_50_99", "50-99"),
                            ("SIZE_100", "100 and Above"),
                        ],
                        max_length=11,
                        null=True,
                        verbose_name="Number of employees",
                    ),
                ),
                ("phone_number", models.CharField(blank=True, max_length=13)),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Updated")),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "verbose_name_plural": "Companies",
                "ordering": ["-created"],
            },
        ),
    ]