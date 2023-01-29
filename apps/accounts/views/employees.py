from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from apps.jobs.models import Application, Job

from ..forms import UserEmployeeEditForm, EmployeeEditForm, ResumeForm
from ..models import Resume


@login_required
def employee_jobs(request):
    applications = Application.objects.filter(applicant=request.user.employee)

    template_name = "employees/jobs.html"
    context = {
        "user": request.user,
        "applications": applications,
    }

    return render(request, template_name, context)


@login_required
def employee_dashboard(request):
    template_name = 'employees/dashboard.html'
    context = {
        'user': request.user,
    }

    return render(request, template_name, context)


@login_required
def employee_messages(request):
    template_name = 'employees/messages.html'
    context = {
        'user': request.user,
    }

    return render(request, template_name, context)


@login_required
def employee_account(request):
    if request.method == 'POST':
        user_form = UserEmployeeEditForm(request.POST, instance=request.user)
        employee_form = EmployeeEditForm(
            request.POST, request.FILES, instance=request.user.employee)
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            messages.success(
                request, "Your account settings have been updated.")
            return redirect('employees:account')
        else:
            messages.warning(request, "An error occured. Please check below.")
    else:
        user_form = UserEmployeeEditForm(instance=request.user)
        employee_form = EmployeeEditForm(instance=request.user.employee)

    template_name = 'employees/account.html'
    context = {
        'user': request.user,
        'user_form': user_form,
        'employee_form': employee_form,
    }

    return render(request, template_name, context)


@login_required
def employee_resume(request):
    try:
        employee_resume = Resume.objects.filter(
            employee=request.user.employee)[:1].get()
    except Resume.DoesNotExist:
        employee_resume = None
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=employee_resume)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.employee = request.user.employee
            resume.save()
            messages.success(request, "Your resume has been saved.")
            return redirect(resume)
        else:
            messages.warning(request, "An error occured. Please check below.")
    else:
        form = ResumeForm(instance=employee_resume)

    template_name = 'employees/resume.html'
    context = {
        'user': request.user,
        'form': form,
    }

    return render(request, template_name, context)


@login_required
def resume_detail(request, id):
    resume = get_object_or_404(Resume, id=id)

    template_name = "employees/resume_detail.html"
    context = {
        "resume": resume,
    }

    return render(request, template_name, context)


@login_required
def employee_bookmarks(request):
    bookmarks = Job.active.filter(bookmarks=request.user.employee)

    template_name = "employees/bookmarks.html"
    context = {
        "bookmarks": bookmarks,
    }

    return render(request, template_name, context)
