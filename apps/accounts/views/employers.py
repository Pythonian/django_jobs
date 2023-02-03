from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from apps.jobs.models import Application, Job

from ..forms import CompanyEditForm


@login_required
def company_account(request):
    if request.method == 'POST':
        form = CompanyEditForm(request.POST, request.FILES,
                               instance=request.user.company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was successfully updated.')
            return redirect('employers:account')
        else:
            messages.warning(request, 'An error occured. Please check below.')
    else:
        form = CompanyEditForm(instance=request.user.company)

    template_name = "employers/account.html"
    context = {
        "user": request.user,
        "form": form,
    }

    return render(request, template_name, context)


@login_required
def company_jobs(request):
    jobs = Job.objects.filter(company=request.user.company)
    template_name = "employers/jobs.html"
    context = {
        "user": request.user,
        "jobs": jobs,
    }

    return render(request, template_name, context)


@login_required
def company_candidates(request):
    jobs = Job.objects.filter(company=request.user.company)
    candidates = Application.objects.filter(job__company=request.user.company)

    template_name = "employers/candidates.html"
    context = {
        "user": request.user,
        "jobs": jobs,
        "candidates": candidates,
    }

    return render(request, template_name, context)
