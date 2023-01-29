from secrets import choice
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import Company, Employee

from .managers import ActiveJobManager
from .utils import image_path


class Category(models.Model):
    name = models.CharField(_('Name'), unique=True, max_length=25)
    slug = models.SlugField(_('Slug'), unique=True, max_length=25)
    description = models.TextField(_('Description'), blank=True)
    image = models.ImageField(_('Image'), upload_to=image_path, blank=True)
    category_order = models.PositiveIntegerField(_('Category order'),
                                                    unique=True, blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['category_order']

    def __str__(self):
        return self.name

    def get_total_jobs(self):
        return Job.active.filter(category=self).count()

    def get_absolute_url(self):
        return reverse('jobs:category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.category_order:
            try:
                self.category_order = Category.objects.\
                                    latest('category_order').category_order + 1
            except Category.DoesNotExist:
                self.category_order = 0
        super().save(*args, **kwargs)


class JobType(models.Model):
    name = models.CharField(_('Name'), unique=True, max_length=15)
    slug = models.SlugField(_('Slug'), unique=True, max_length=15)

    class Meta:
        verbose_name = _('Job Type')
        verbose_name_plural = _('Job Types')
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_total_jobs(self):
        return Job.active.filter(jobtype=self).count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class State(models.Model):
    name = models.CharField(_('Name'), unique=True, max_length=25)
    slug = models.SlugField(_('Slug'), unique=True, max_length=25)

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_total_jobs(self):
        return Job.active.filter(state=self).count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Job(models.Model):

    class JobStatus(models.TextChoices):
        ACTIVE = 'A', _('Active')
        INACTIVE = 'I', _('Inactive')
        # ARCHIVED by employer

    class SalarySchedule(models.TextChoices):
        HOURLY = 'H', _('Hourly')
        DAILY = 'D', _('Daily')
        WEEKLY = 'W', _('Weekly')
        MONTHLY = 'M', _('Monthly')
        YEARLY = 'Y', _('Yearly')

    class GenderStatus(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, unique=True)
    description = models.TextField(_('Description')) # use RichTextEditor
    salary_mode = models.CharField(
        _('Salary Mode'), max_length=1, choices=SalarySchedule.choices)
    base_salary_amount = models.PositiveIntegerField()
    maximum_salary_amount = models.PositiveIntegerField(blank=True, null=True)
    experience = models.PositiveIntegerField(_('Years of experience'),
                                             blank=True, null=True)
    vacancy = models.PositiveIntegerField(blank=True, null=True)
    application_deadline = models.DateField()
    qualification_title = models.CharField(_('Qualification title'), max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=GenderStatus.choices, blank=True)
    status = models.CharField(
        max_length=1, choices=JobStatus.choices, default=JobStatus.ACTIVE)
    
    category = models.ForeignKey(Category, verbose_name=_('Category'), null=True,
                                 related_name='jobs', on_delete=models.SET_NULL)
    jobtype = models.ForeignKey(JobType, verbose_name=_('Job Type'), null=True,
                                on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, verbose_name=_('Company'),
                                related_name='jobs', on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    state = models.ForeignKey(State, verbose_name=_('State'), null=True,
                              on_delete=models.SET_NULL)
    applicants = models.ManyToManyField(
        Employee, related_name='applicants', blank=True, default=None)
    bookmarks = models.ManyToManyField(
        Employee, related_name='bookmarks', blank=True)

    impressions = models.PositiveIntegerField(default=0)
    sponsored = models.BooleanField(_('Sponsored'), default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active = ActiveJobManager()

    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')
        ordering = ['application_deadline', '-created']

    def __str__(self):
        """Return the string representation of the model"""
        return self.title

    # @classmethod
    # def job_count(cls):
    #     return cls.objects.filter(status=JobStatus.ACTIVE).count()

    def get_absolute_url(self):
        return reverse('jobs:detail', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse('jobs:edit', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('jobs:delete', kwargs={'id': self.id})

    # def get_application_count(self):
    #     return Applicant.objects.filter(job=self).count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Application(models.Model):

    class ApplicationStatus(models.TextChoices):
        PENDING = 'P', _('Pending')
        ACCEPTED = 'A', _('Accepted')
        REJECTED = 'R', _('Rejected')

    job = models.ForeignKey(
        Job, related_name='applications', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        Employee, related_name='applications', on_delete=models.CASCADE)
    note = models.TextField(max_length=500)
    status = models.CharField(
        max_length=1, choices=ApplicationStatus.choices, default=ApplicationStatus.PENDING)
    # cover_letter = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.applicant} applied for {self.job}"
