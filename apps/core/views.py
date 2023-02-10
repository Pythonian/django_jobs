from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from apps.accounts.models import Company, Resume
from apps.core.utils import mk_paginator
from apps.jobs.models import Job, State, Category


def home(request):
    """
    Returns the Home page.

    Template: ``core/home.html``
    """

    # TODO: Use template tags to display the listings and randomize them
    jobs = Job.active.all()[:4]
    companies = Company.objects.filter(jobs__isnull=False).distinct()[:6]
    resumes = Resume.objects.all()
    categories = Category.objects.all()[:8]

    template = 'core/home.html'
    context = {
        'jobs': jobs,
        'jobs_count': Job.active.all().count(),
        'companies': companies,
        'companies_count': Company.objects.all().count(),
        'states_count': State.objects.all().count(),
        'resumes': resumes,
        'resumes_count': Resume.objects.all().count(),
        'categories': categories,
    }

    return render(request, template, context)


@login_required
def dashboard(request):
    if request.user.is_company:
        return redirect('employers:account')
    elif request.user.is_employee:
        return redirect('employees:dashboard')
    else:
        return redirect('core:home')


def companies(request):
    """
    Returns the page for viewing all companies.

    Template: ``companies/company_list.html``
    Context:
        companies
            A list of registered Company objects
    """

    # retrieve only companies with at least one job, and ensure
    # each company is listed just once even if it has multiple jobs
    # TODO: filter down by only active jobs
    companies = Company.objects.filter(jobs__isnull=False).distinct()
    companies = mk_paginator(request, companies, 12)

    template = 'core/companies.html'
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

    template = 'employers/detail.html'
    context = {
        'company': company,
        'jobs': jobs,
        # 'last_seen': request.user.last_seen,
    }

    return render(request, template, context)


def resumes(request):
    resumes = Resume.objects.all()
    resumes = mk_paginator(request, resumes, 12)

    template = 'core/resumes.html'
    context = {
        'resumes': resumes,
    }

    return render(request, template, context)


def categories(request):

    categories = Category.objects.all()

    template = 'core/categories.html'
    context = {
        'categories': categories,
    }

    return render(request, template, context)


def category_detail(request, slug):
    """
    Returns the detail page of a category.

    Template: ``category_detail.html``
    Context:
        category
            A category object instance
    """
    category = get_object_or_404(Category, slug=slug)
    jobs = category.jobs.all()

    template = 'core/category_detail.html'
    context = {
        'category': category,
        'jobs': jobs,
    }

    return render(request, template, context)


def help_center(request):

    template = 'core/help-center.html'
    context = {

    }

    return render(request, template, context)


def help_article(request):

    template = 'core/help-article.html'
    context = {

    }

    return render(request, template, context)


def help_category(request):

    template = 'core/help-category.html'
    context = {

    }

    return render(request, template, context)


def faq(request):

    template = 'core/faq.html'
    context = {

    }

    return render(request, template, context)


def about(request):

    template = 'core/about.html'
    context = {

    }

    return render(request, template, context)


def policy(request):

    template = 'core/policy.html'
    context = {

    }

    return render(request, template, context)
