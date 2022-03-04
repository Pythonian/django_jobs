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


# def job_list(request):
#     job_list = Job.objects.all()

#     return render(
#         request, 'job_list.html', {'job_list': job_list})


# def job_detail(request, slug):
#     job = get_object_or_404(Job, slug=slug)

#     if request.method == 'POST':
#         form = ApplicationForm(request.POST)
#         if form.is_valid():
#             apply = form.save(commit=False)
#             apply.job = job
#             apply.applicant = request.user
#             apply.save()
#             messages.success(
#                 request, "Your application request was sent.")
#             return redirect('job_detail', job.slug)
#     else:
#         form = ApplicationForm()

#     return render(
#         request, 'job_detail.html',
#         {'job': job, 'form': form})


# @login_required
# def job_create(request):
#     if request.method == 'POST':
#         form = JobForm(request.POST)
#         if form.is_valid():
#             job = form.save(commit=False)
#             job.company = request.user
#             job.save()
#             return redirect(job_detail)
#     else:
#         form = JobForm()

#     return render(request, 'create_job.html', {'form': form})


# def job_applications(request):
#     pass
