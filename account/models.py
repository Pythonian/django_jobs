from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('Company name', max_length=100, unique=True)
    # slug = models.SlugField(max_length=100, unique=True)
    about = models.TextField(max_length=5000)
    logo = models.ImageField(upload_to='logos', blank=True) # crop logo to 80x80
    contact_person = models.CharField(max_length=255)
    position_in_company = models.CharField(max_length=50)
    established = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True)
    staff_strength = models.CharField('Number of employees', max_length=50, blank=True)
    phone_number = models.CharField(max_length=13, blank=True)
    # industry
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.user.username


# class Employee(models.Model):
#     MALE = 'M'
#     FEMALE = 'F'
#     GENDER_CHOICES = (
#         (MALE, 'Male'),
#         (FEMALE, 'Female'),
#     )

#     PRIMARY_SCHOOL = 'PS'
#     SECONDARY_SCHOOL = 'SS'
#     COLLEGE_EDUCATION = 'CE'
#     POLYTECHNIC = 'PO'
#     UNIVERSITY = 'UI'
#     EDUCATION_LEVEL_CHOICES = (
#         (PRIMARY_SCHOOL, 'Primary School'),
#         (SECONDARY_SCHOOL, 'Secondary School'),
#         (COLLEGE_EDUCATION, 'College of Education'),
#         (POLYTECHNIC, 'Polytechnic'),
#         (UNIVERSITY, 'University'))

#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name='applicant')
#     date_of_birth = models.DateField(blank=True, null=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     phone_number = models.CharField(max_length=13, blank=True)
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     about = models.TextField()
#     education_level = models.CharField(
#         max_length=2, choices=EDUCATION_LEVEL_CHOICES)
#     cv = models.FileField('Upload CV', upload_to='cvs', blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='applicants', blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.username

# class Experience(models.Model):
#     user = models.ForeignKey(
#         Applicant, on_delete=models.CASCADE, related_name='experiences')
#     company_name = models.CharField(max_length=50)
#     job_title = models.CharField(max_length=50)
#     supervisor_name = models.CharField(
#         max_length=50, blank=True, null=True)
#     supervisor_email = models.EmailField(blank=True, null=True)
#     task_description = models.TextField()
#     year = models.DateField()
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-created']

#     def __str__(self):
#         return self.job_title


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
