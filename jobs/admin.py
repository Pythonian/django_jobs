from django.contrib import admin
from .models import (
    Category, State, Company, Applicant, Job, Experience,
    LanguageProficiency, AcquiredSkill, Application)


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1


class LanguageProficiencyInline(admin.StackedInline):
    model = LanguageProficiency
    extra = 1


class AcquiredSkillInline(admin.StackedInline):
    model = AcquiredSkill
    extra = 1


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company',
                    'job_type', 'vacancy', 'state', 'application_deadline']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'company', 'state']
    list_filter = ['job_type', 'company__category']


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'state',
                    'phone_number', 'education_level']
    search_fields = ['user']
    list_filter = ['gender', 'education_level']
    inlines = [ExperienceInline, LanguageProficiencyInline,
               AcquiredSkillInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'state', 'established']
    list_filter = ['category']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Application)
