from datetime import date
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.utils import timezone


def user_directory_path(instance, filename):
    return f'users/avatars/{instance.user.id}/{filename}'

class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    last_seen = models.DateTimeField(default=timezone.now)


class Company(models.Model):

    class StaffStrength(models.TextChoices):
        SIZE_1_9 = 'SIZE_1_9', _('1-9')
        SIZE_10_49 = 'SIZE_10_49', _('10-49')
        SIZE_50_99 = 'SIZE_50_99', _('50-99')
        SIZE_100 = 'SIZE_100', _('100 and Above')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('Company name', max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    about = models.TextField(max_length=5000)
    logo = models.ImageField(upload_to='logos', blank=True, default='img/avatar.svg') # crop logo to 80x80
    contact_person = models.CharField(max_length=255)
    position_in_company = models.CharField(max_length=50)
    established = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True)
    staff_strength = models.CharField(
        _('Number of employees'), max_length=11, choices=StaffStrength.choices, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # def clean(self):
    #     if not self.logo:
    #         raise ValidationError('x')
    #     else:
    #         w, h = get_image_dimensions(self.logo)
    #         if w != 200:
    #             raise ValidationError('x')
    #         if h!= 200:
    #             raise ValidationError('x')


class Employee(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=13, blank=True)
    location = models.CharField(max_length=50)
    about = models.TextField() # remove?
    image = models.ImageField(upload_to='employees', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def age(self):
        today = date.today()
        if self.date_of_birth:
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


class Resume(models.Model):
    PRIMARY_SCHOOL = 'PS'
    SECONDARY_SCHOOL = 'SS'
    COLLEGE_EDUCATION = 'CE'
    POLYTECHNIC = 'PO'
    UNIVERSITY = 'UI'
    VOCATIONAL = 'VO'
    EDUCATION_LEVEL_CHOICES = (
        (PRIMARY_SCHOOL, 'Primary School'),
        (SECONDARY_SCHOOL, 'Secondary School'),
        (VOCATIONAL, 'Vocational School'),
        (COLLEGE_EDUCATION, 'College of Education'),
        (POLYTECHNIC, 'Polytechnic'),
        (UNIVERSITY, 'University'))

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    professional_title = models.CharField(max_length=50)
    professional_summary_or_objective = models.TextField(max_length=1000)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, blank=True)
    language_spoken = models.CharField(max_length=200, blank=True)
    website = models.URLField('Personal website or blog')

    # Last Experience
    company_name = models.CharField(max_length=50)
    company_description = models.TextField(blank=True)
    job_title = models.CharField('Job title or Position', max_length=50)
    supervisor_name = models.CharField(
        max_length=50, blank=True, null=True)
    supervisor_email = models.EmailField(blank=True, null=True)
    task_description = models.TextField('Achievements or Responsibilities')
    year_started = models.PositiveIntegerField()
    year_ended = models.PositiveIntegerField()
    location = models.CharField(max_length=50)

    # Last School
    education_level = models.CharField(
        max_length=2, choices=EDUCATION_LEVEL_CHOICES)
    name_of_institution = models.CharField(max_length=50)
    year_of_admission = models.PositiveIntegerField()
    year_of_graudation = models.PositiveIntegerField()
    course_of_study = models.CharField(max_length=50)

    class Meta:
        ordering = ['professional_title']

    def __str__(self):
        return f'{self.employee.user.username} - {self.professional_title}'

    def get_absolute_url(self):
        return reverse('resume_detail', kwargs={'id': self.id})


class Experience(models.Model):
    resume = models.OneToOneField(
        Resume, on_delete=models.CASCADE, related_name='experiences')
    company_name = models.CharField(max_length=50)
    company_description = models.TextField(blank=True)
    job_title = models.CharField('Job title or Position', max_length=50)
    supervisor_name = models.CharField(
        max_length=50, blank=True, null=True)
    supervisor_email = models.EmailField(blank=True, null=True)
    task_description = models.TextField('Achievements or Responsibilities')
    year_started = models.PositiveIntegerField()
    year_ended = models.PositiveIntegerField()
    location = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.job_title


class Education(models.Model):
    PRIMARY_SCHOOL = 'PS'
    SECONDARY_SCHOOL = 'SS'
    COLLEGE_EDUCATION = 'CE'
    POLYTECHNIC = 'PO'
    UNIVERSITY = 'UI'
    VOCATIONAL = 'VO'
    EDUCATION_LEVEL_CHOICES = (
        (PRIMARY_SCHOOL, 'Primary School'),
        (SECONDARY_SCHOOL, 'Secondary School'),
        (VOCATIONAL, 'Vocational School'),
        (COLLEGE_EDUCATION, 'College of Education'),
        (POLYTECHNIC, 'Polytechnic'),
        (UNIVERSITY, 'University'))

    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='education')
    education_level = models.CharField(
        max_length=2, choices=EDUCATION_LEVEL_CHOICES)
    name_of_institution = models.CharField(max_length=50)
    year_of_admission = models.PositiveIntegerField() #MaxLengthValidation
    year_of_graudation = models.PositiveIntegerField()
    course_of_study = models.CharField(max_length=50)

    def __str__(self):
        return self.name_of_institution

# class LanguageProficiency(models.Model):
#     ENGLISH = 'E'
#     IGBO = 'I'
#     HAUSA = 'H'
#     YORUBA = 'Y'
#     LANGUAGE_CHOICES = (
#         (ENGLISH, 'English'),
#         (IGBO, 'Igbo'),
#         (HAUSA, 'Hausa'),
#         (YORUBA, 'Yoruba'))

#     FAIR = 'F'
#     GOOD = 'G'
#     VERYGOOD = 'V'
#     ABILITY_LEVEL_CHOICES = (
#         (FAIR, 'Fair'),
#         (GOOD, 'Good'),
#         (VERYGOOD, 'Very Good'))

#     user = models.ForeignKey(
#         Applicant, on_delete=models.CASCADE, related_name='languages')
#     language = models.CharField(max_length=1, choices=LANGUAGE_CHOICES)
#     ability_level = models.CharField(
#         max_length=1, choices=ABILITY_LEVEL_CHOICES)


# class AcquiredSkill(models.Model):
#     FAIR = 'F'
#     GOOD = 'G'
#     VERYGOOD = 'V'
#     ABILITY_LEVEL_CHOICES = (
#         (FAIR, 'Fair'),
#         (GOOD, 'Good'),
#         (VERYGOOD, 'Very Good'))

#     user = models.ForeignKey(
#         Applicant, on_delete=models.CASCADE, related_name='skills')
#     skill = models.CharField(max_length=50)
#     ability_level = models.CharField(
#         max_length=1, choices=ABILITY_LEVEL_CHOICES)
#     relevant_certificate = models.FileField(
#         upload_to='certificates', blank=True, null=True)
