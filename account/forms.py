from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignupForm(forms.ModelForm):
    ACCOUNT_CHOICES = ''
    account_type = forms.CharField(widget=forms.RadioSelect(choices=ACCOUNT_CHOICES))

    class Meta:
        model = UserCreationForm