from django import forms

from .models import Apply, Job


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['note']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'category', 'job_type', 'description',
                  'salary', 'experience', 'location']
