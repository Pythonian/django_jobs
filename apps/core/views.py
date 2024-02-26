from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from apps.accounts.models import Company, Resume
from apps.core.utils import mk_paginator
from apps.jobs.models import Job, State, Category

from .models import Testimonial


def home(request):
    """
    Returns the Home page.

    Template: ``core/home.html``
    """

    # TODO: Use template tags to display the listings and randomize them
    jobs = Job.active.all()[:4]
    companies = Company.objects.filter(jobs__isnull=False).distinct()[:6]
    resumes = Resume.objects.all()[:5]
    categories = Category.objects.all()[:8]
    testimonials = Testimonial.objects.all()[:3]

    template = "core/home.html"
    context = {
        "jobs": jobs,
        "jobs_count": Job.active.all().count(),
        "companies": companies,
        "companies_count": Company.objects.all().count(),
        "states_count": State.objects.all().count(),
        "resumes": resumes,
        "resumes_count": Resume.objects.all().count(),
        "categories": categories,
        "testimonials": testimonials,
    }

    return render(request, template, context)


@login_required
def dashboard(request):
    if request.user.is_company:
        return redirect("employers:account")
    elif request.user.is_employee:
        return redirect("employees:dashboard")
    else:
        return redirect("core:home")


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

    template = "core/companies.html"
    context = {
        "companies": companies,
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

    template = "employers/detail.html"
    context = {
        "company": company,
        "jobs": jobs,
        # 'last_seen': request.user.last_seen,
    }

    return render(request, template, context)


def resumes(request):
    resumes = Resume.objects.all()
    resumes = mk_paginator(request, resumes, 12)

    template = "core/resumes.html"
    context = {
        "resumes": resumes,
    }

    return render(request, template, context)


def faq(request):

    template = "core/faq.html"
    context = {}

    return render(request, template, context)


class AboutView(TemplateView):
    template_name = "core/about.html"


class PolicyView(TemplateView):
    template_name = "core/policy.html"


def post(request):

    template = "core/post.html"
    context = {}

    return render(request, template, context)


def contact(request):

    template = "core/contact.html"
    context = {}

    return render(request, template, context)


############################################
#               ERROR PAGES                #
############################################


def error_500(request):
    return render(request, "500.html")


def error_404(request, exception):
    return render(request, "404.html")
