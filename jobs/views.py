from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Job, Company, Category, Applicant
from .forms import ApplicationForm, JobForm


def home(request):
    jobs = Job.objects.all()
    categories = Category.objects.all()
    companies = Company.objects.all()
    job_seekers = Applicant.objects.all()

    return render(
        request, 'home.html', {'jobs': jobs,
                               'categories': categories,
                               'companies': companies,
                               'job_seekers': job_seekers})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    jobs = Job.objects.filter(company__category=category)

    return render(
        request, 'category_detail.html', {'category': category,
                                          'jobs': jobs})


def job_list(request):
    jobs = Job.objects.all()

    return render(
        request, 'job_list.html', {'jobs': jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    applicants = job.applications.all()

    # if request.method == 'POST':
    #     form = ApplicationForm(request.POST)
    #     if form.is_valid():
    #         apply = form.save(commit=False)
    #         apply.job = job
    #         apply.applicant = request.user
    #         apply.save()
    #         messages.success(
    #             request, "Your application request was sent.")
    #         return redirect('job_detail', job.slug)
    # else:
    #     form = ApplicationForm()

    return render(
        request, 'job_detail.html',
        {'job': job, 'applicants': applicants})


def companies(request):
    companies = Company.objects.all()

    return render(
        request, 'companies.html', {'companies': companies})


def company_detail(request, id):
    company = get_object_or_404(Company, id=id)
    jobs = company.jobs.all()

    return render(
        request, 'company_detail.html',
        {'company': company, 'jobs': jobs})


@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user
            job.save()
            return redirect('job_detail', job.id)
    else:
        form = JobForm()

    return render(request, 'job_create.html', {'form': form})


# def job_applications(request):
#     pass
