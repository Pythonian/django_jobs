from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from account.models import Company
from jobs.models import Job, State


def home(request):
    jobs = Job.active.all()[:4]
    companies = Company.objects.all()[:6]
    # resumes = Applicant.objects.all()

    template = 'home.html'
    context = {
        'jobs': jobs,
        'companies': companies,
        'states': State.objects.all().count(),
        # 'resumes': resumes,
    }

    return render(request, template, context)


# @login_required
# def profile(request):
#     if request.user.is_company:
#         return render(request, 'company_account.html')
