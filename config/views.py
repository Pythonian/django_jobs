from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.accounts.models import Company, Resume
from apps.jobs.models import Job, State
from apps.jobs.utils import mk_paginator


def home(request):
    """
    Returns the Home page.

    Template: ``core/home.html``
    """

    # TODO: Use template tags to display the listings
    jobs = Job.active.all()[:4]
    companies = Company.objects.all()[:6]
    resumes = Resume.objects.all()

    template = 'core/home.html'
    context = {
        'jobs': jobs,
        'jobs_count': Job.active.all().count(),
        'companies': companies,
        'companies_count': Company.objects.all().count(),
        'states_count': State.objects.all().count(),
        'resumes': resumes,
        'resumes_count': Resume.objects.all().count(),
    }

    return render(request, template, context)


@login_required
def dashboard(request):
    if request.user.is_company:
        return redirect('company_account')
    elif request.user.is_employee:
        return redirect('employee_dashboard')
    else:
        return redirect('home')


def companies(request):
    """
    Returns the page for viewing all companies.

    Template: ``companies/company_list.html``
    Context:
        companies
            A list of registered Company objects
    """

    companies = Company.objects.all()
    companies = mk_paginator(request, companies, 12)

    template = 'companies.html'
    context = {
        'companies': companies,
    }

    return render(request, template, context)


def company_detail(request, slug):
    """
    Returns the detail page of a company.

    Template: ``company_detail.html``
    Context:
        company
            A company object instance
    """
    company = get_object_or_404(Company, slug=slug)
    jobs = company.jobs.all()

    template = 'company_detail.html'
    context = {
        'company': company,
        'jobs': jobs
    }

    return render(request, template, context)


def resumes(request):
    resumes = Resume.objects.all()
    resumes = mk_paginator(request, resumes, 12)

    template = 'resumes.html'
    context = {
        'resumes': resumes,
    }

    return render(request, template, context)
