from django import forms

from .models import Application, Job


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['note']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'job_type', 'description', 'salary']
