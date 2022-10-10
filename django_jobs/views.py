from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from account.models import Company
from jobs.models import Job, State
from jobs.utils import mk_paginator


def home(request):
    # TODO: Use template tags to display the listings
    jobs = Job.active.all()[:4]
    companies = Company.objects.all()[:6]
    # resumes = Applicant.objects.all()

    template = 'home.html'
    context = {
        'jobs': jobs,
        'jobs_count': Job.active.all().count(),
        'companies': companies,
        'companies_count': Company.objects.all().count(),
        'states_count': State.objects.all().count(),
        # 'resumes': resumes,
    }

    return render(request, template, context)


def companies(request):
    companies = Company.objects.all()
    companies = mk_paginator(request, companies, 12)

    template = 'companies.html'
    context = {
        'companies': companies,
    }

    return render(request, template, context)


def company_detail(request, slug):
    company = get_object_or_404(Company, slug=slug)
    jobs = company.jobs.all()

    template = 'company_detail.html'
    context = {
        'company': company,
        'jobs': jobs
    }

    return render(request, template, context)


# @login_required
# def profile(request):
#     if request.user.is_company:
#         return render(request, 'company_account.html')
