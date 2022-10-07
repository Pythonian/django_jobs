from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .forms import CompanySignupForm


def signup_choice(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'registration/signup_choice.html', {})


def signup_employer(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CompanySignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='account.backends.EmailAuthenticationBackend')
            messages.success(
                request, "Signup successful. Please confirm account.")
            # Send welcome email to employer
            return redirect('home')
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


def signup(request):
    # if request.user.is_authenticated:
    #     return redirect("home")
    # if request.method == "POST":
    #     form = StudentSignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         email = form.cleaned_data.get('email')
    #         split_email = email.split('@')
    #         user.username = split_email[0]
    #         user.is_student = True
    #         user.save()
    #         user.refresh_from_db()
    #         user.student.phone_number = form.cleaned_data.get('phone_number')
    #         user.save()
    #         login(request, user)
    #         messages.success(
    #             request, "Signup successful.")
    #         return redirect("home")
    #     else:
    #         messages.warning(
    #             request, "An error occured. Please check below.")
    # else:
    #     form = StudentSignUpForm()

    template_name = "registration/signup.html"
    context = {
        # "form": form,
    }

    return render(request, template_name, context)


@login_required
def company_account(request):

    template_name = "company_account.html"
    context = {
        "user": request.user,
    }

    return render(request, template_name, context)


@login_required
def company_jobs(request):

    template_name = "company_jobs.html"
    context = {
        "user": request.user,
    }

    return render(request, template_name, context)


@login_required
def company_candidates(request):

    template_name = "company_candidates.html"
    context = {
        "user": request.user,
    }

    return render(request, template_name, context)

# @login_required
class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('password_change')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was successfully changed.')
        return super().form_valid(form)
