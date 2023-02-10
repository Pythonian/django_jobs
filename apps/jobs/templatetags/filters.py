from django import template
from django.utils.translation import gettext_lazy as _

from ..models import Job

register = template.Library()


@register.filter
def get_salary_mode_display(value):
    choices = dict(Job.SalarySchedule.choices)
    return choices.get(value, '')
