from django.db import models
from django.utils.text import slugify
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    about = models.TextField(max_length=5000)
    logo = models.ImageField(upload_to='logos', blank=True)
    company_email = models.EmailField()
    established = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=13,
                                    blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Applicant(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    PRIMARY_SCHOOL = 'PS'
    SECONDARY_SCHOOL = 'SS'
    COLLEGE_EDUCATION = 'CE'
    POLYTECHNIC = 'PO'
    UNIVERSITY = 'UI'
    EDUCATION_LEVEL_CHOICES = (
        (PRIMARY_SCHOOL, 'Primary School'),
        (SECONDARY_SCHOOL, 'Secondary School'),
        (COLLEGE_EDUCATION, 'College of Education'),
        (POLYTECHNIC, 'Polytechnic'),
        (UNIVERSITY, 'University'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=13, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    about = models.TextField()
    education_level = models.CharField(
        max_length=2, choices=EDUCATION_LEVEL_CHOICES)
    cv = models.FileField('Upload CV', upload_to='cvs', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='applicants', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Job(models.Model):
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    FREELANCER = 'FL'
    INTERNSHIP = 'IT'
    JOB_TYPE = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (FREELANCER, 'Freelancer'),
        (INTERNSHIP, 'Internship'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    company = models.ForeignKey(
        Company, related_name='companies', on_delete=models.CASCADE)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    salary = models.CharField(max_length=25)
    years_of_experience = models.IntegerField()
    vacancy = models.IntegerField(default=1)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    application_deadline = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Experience(models.Model):
    user = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name='experiences')
    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    supervisor_name = models.CharField(
        max_length=50, blank=True, null=True)
    supervisor_email = models.EmailField(blank=True, null=True)
    task_description = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.job_title


class LanguageProficiency(models.Model):
    ENGLISH = 'E'
    IGBO = 'I'
    HAUSA = 'H'
    YORUBA = 'Y'
    LANGUAGE_CHOICES = (
        (ENGLISH, 'English'),
        (IGBO, 'Igbo'),
        (HAUSA, 'Hausa'),
        (YORUBA, 'Yoruba'))

    FAIR = 'F'
    GOOD = 'G'
    VERYGOOD = 'V'
    ABILITY_LEVEL_CHOICES = (
        (FAIR, 'Fair'),
        (GOOD, 'Good'),
        (VERYGOOD, 'Very Good'))

    user = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name='languages')
    language = models.CharField(max_length=1, choices=LANGUAGE_CHOICES)
    ability_level = models.CharField(
        max_length=1, choices=ABILITY_LEVEL_CHOICES)


class AcquiredSkill(models.Model):
    FAIR = 'F'
    GOOD = 'G'
    VERYGOOD = 'V'
    ABILITY_LEVEL_CHOICES = (
        (FAIR, 'Fair'),
        (GOOD, 'Good'),
        (VERYGOOD, 'Very Good'))

    user = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name='skills')
    skill = models.CharField(max_length=50)
    ability_level = models.CharField(
        max_length=1, choices=ABILITY_LEVEL_CHOICES)
    relevant_certificate = models.FileField(
        upload_to='certificates', blank=True, null=True)


class Application(models.Model):
    job = models.ForeignKey(
        Job, related_name='apply_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='job_applicant', on_delete=models.CASCADE)
    note = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.applicant} applied for {self.job}"
