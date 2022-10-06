from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def signup_choice(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'registration/signup_choice.html', {})


def signup_employer(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'registration/signup_employer.html', {})


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
