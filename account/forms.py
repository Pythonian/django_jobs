from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.utils.text import slugify

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from crispy_bootstrap5.bootstrap5 import FloatingField

from .models import User


class UserLoginForm(AuthenticationForm):
    """ Custom Login form that extends Django's Login form. """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.EmailField(
        label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CompanySignupForm(UserCreationForm):
    email = forms.EmailField()
    established = forms.DateField(widget=forms.DateInput)
    position_in_company = forms.CharField()
    about = forms.CharField(label='', widget=forms.Textarea)
    staff_strength = forms.CharField()
    address = forms.CharField()
    website = forms.CharField(required=False)
    phone_number = forms.CharField()
    contact_person = forms.CharField(label='Contact Fullname')
    name = forms.CharField(label='Company name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.help_text = None
        self.fields['about'].widget.attrs = {'rows': 4}
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(FloatingField('contact_person'), css_class='form-group col-lg-3 mb-0'),
                Column(FloatingField('position_in_company'), css_class='form-group col-lg-3 mb-0'),
                Column(FloatingField('email'), css_class='form-group col-lg-3 mb-0'),
                Column(FloatingField('phone_number'), css_class='form-group col-lg-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(FloatingField('password1'), css_class='form-group col-lg-6 mb-0'),
                Column(FloatingField('password2'), css_class='form-group col-lg-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(FloatingField('name'), css_class='form-group col-lg-6 mb-0'),
                Column(FloatingField('staff_strength'), css_class='form-group col-lg-2 mb-0'),
                Column(FloatingField('established'), css_class='form-group col-lg-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(FloatingField('address'), css_class='form-group col-lg-8 mb-0'),
                Column(FloatingField('website'), css_class='form-group col-lg-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('about', css_class='form-group col-12'),
                css_class='form-row'
            ),
            Submit('submit', 'Create account')
        )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['contact_person', 'email', 'password1', 'password2', 'staff_strength',
                  'name', 'about', 'phone_number', 'address', 'website', 'established']
        widgets = {
            'established': forms.DateInput(
                attrs={
                    'type': 'date', 
                    'onkeydown': 'return false',}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "A user with that email already exists.")
        return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        email = self.cleaned_data.get('email')
        split_email = email.split('@')
        user.username = split_email[0]
        user.is_company = True
        user.save()
        user.refresh_from_db()
        user.company.about = self.cleaned_data.get('about')
        user.company.position_in_company = self.cleaned_data.get('position_in_company')
        user.company.phone_number = self.cleaned_data.get('phone_number')
        user.company.contact_person = self.cleaned_data.get('contact_person')
        user.company.staff_strength = self.cleaned_data.get('staff_strength')
        user.company.company_name = self.cleaned_data.get('company_name')
        user.company.name = self.cleaned_data.get('name')
        user.company.address = self.cleaned_data.get('address')
        user.company.website = self.cleaned_data.get('website')
        user.company.established = self.cleaned_data.get('established')
        user.save()
        return user


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget = forms.widgets.EmailInput(attrs={
        #         'class': 'form-control'})
        # self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
        #         'class': 'form-control'})
        for field in self.visible_fields():
            field.help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "A user with that email already exists.")
        return email
