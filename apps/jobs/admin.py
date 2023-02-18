from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Category, Job, JobType, State, Application


def mark_sponsored(modeladmin, request, queryset):
    queryset.update(sponsored=True)
mark_sponsored.short_description = _('Mark selected jobs as sponsored.')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_order']


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'jobtype', 'state', 'category', 'application_deadline',
                    'sponsored', 'status']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'company', 'state', 'category']
    list_filter = ['status']
    actions = [mark_sponsored]

# from .models import (
#     , , Company, Applicant, Experience,
#     LanguageProficiency, AcquiredSkill, Application)


# class ExperienceInline(admin.StackedInline):
#     model = Experience
#     extra = 1


# class LanguageProficiencyInline(admin.StackedInline):
#     model = LanguageProficiency
#     extra = 1


# class AcquiredSkillInline(admin.StackedInline):
#     model = AcquiredSkill
#     extra = 1


# @admin.register(Applicant)
# class ApplicantAdmin(admin.ModelAdmin):
#     list_display = ['user', 'gender', 'state',
#                     'phone_number', 'education_level']
#     search_fields = ['user']
#     list_filter = ['gender', 'education_level']
#     inlines = [ExperienceInline, LanguageProficiencyInline,
#                AcquiredSkillInline]


# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'state', 'established']
#     list_filter = ['category']
#     search_fields = ['name']
#     prepopulated_fields = {'slug': ('name',)}


admin.site.register(Application)
