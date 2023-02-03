from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils import timezone

from ..decorators import anonymous_required
from ..forms import CompanySignupForm, EmployeeSignUpForm
from ..tokens import account_activation_token

User = get_user_model()


@anonymous_required
def signup_choice(request):
    return render(request, 'registration/signup_choice.html', {})


@anonymous_required
def signup_employer(request):
    if request.method == 'POST':
        form = CompanySignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='apps.accounts.backends.EmailAuthenticationBackend')
            messages.success(
                request, "Signup successful. Please confirm account.")
            # Send welcome email to employer
            return redirect('employers:account')
        else:
            messages.warning(
                request, "An error occured. Please check below.")
    else:
        form = CompanySignupForm()

    template_name = 'registration/signup_employer.html'
    context = {
        'form': form,
    }

    return render(request, template_name, context)


@anonymous_required
def signup_employee(request):
    if request.method == "POST":
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_employee = True
            user.email_verified = False
            user.save()

            current_site = get_current_site(request)
            if request.is_secure():
                protocol = 'https'
            else:
                protocol = 'http'
            subject = render_to_string(
                'registration/account_activation_subject.txt',
                {'site_name': current_site.name}
            )
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'protocol': protocol,
                'site_name': current_site.name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)

            login(request, user, backend='apps.accounts.backends.EmailAuthenticationBackend')
            messages.success(
                request, "Signup successful. Please confirm your email address.")
            return redirect('employees:dashboard')
        else:
            messages.warning(
                request, "An error occured. Please check below.")
    else:
        form = EmployeeSignUpForm()

    template_name = "registration/signup_employee.html"
    context = {
        "form": form,
    }

    return render(request, template_name, context)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_verified = True
        user.save()
        login(request, user, backend='apps.accounts.backends.EmailAuthenticationBackend')
        messages.success(
            request, 'Your email address has been successully confirmed.')
        return redirect('employees:dashboard')
    else:
        template_name = "registration/activation_invalid.html"
        context = {}
        return render(request, template_name, context)


class CustomPasswordChangeView(PasswordChangeView): #login_required
    success_url = reverse_lazy('auth:password_change')

    def form_valid(self, form):
        messages.success(
            self.request, 'Your password was successfully changed.')
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


def update_last_seen(request):
    if request.user.is_authenticated:
        request.user.last_seen = timezone.now()
        request.user.save()
