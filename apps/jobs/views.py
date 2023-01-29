from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobForm, ApplicationForm
from .models import Job
from .utils import mk_paginator, is_valid_query_paramter


@login_required
def job_create(request):
    """
    Returns the form page for creating a Job.

    Template: ``jobs/job_form.html``
    Context:
        form
            JobForm object
    """
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company
            job.save()
            messages.success(request, "Job details saved.")
            return redirect(job)
        else:
            messages.warning(request, "An error occured below.")
    else:
        form = JobForm()

    template = 'job_create.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def job_list(request):
    """
    Returns the page for viewing all leads.

    Template: ``leads/lead_list.html``
    Context:
        leads
            A list of active Lead objects
    """
    jobs = Job.active.all()
    jobs = mk_paginator(request, jobs, 5)

    template = 'jobs.html'
    context = {
        'jobs': jobs,
    }

    return render(request, template, context)


def job_detail(request, slug):
    """
    Returns the detail page of a Lead.

    Template: ``leads/lead_detail.html``
    Context:
        lead
            A Lead object instance
    """
    job = get_object_or_404(Job, slug=slug)

    # Create a session key for a user
    session_key = 'viewed_job_{}'.format(job.pk)
    if not request.session.get(session_key, False):
        job.impressions += 1
        job.save()
        request.session[session_key] = True
    applicants = job.applications.count()

    applied = bool
    if request.user.is_authenticated:
        
        if job.applicants.filter(id=request.user.employee.id).exists():
            applied = True

    bookmarked = bool
    if request.user.is_authenticated:

        if job.bookmarks.filter(id=request.user.employee.id).exists():
            bookmarked = True

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user.employee
            application.save()
            job.applicants.add(request.user.employee)
            messages.success(
                request, "Your application request was sent.")
            return redirect(job)
    else:
        form = ApplicationForm()

    template = 'job_detail.html'
    context = {
        'job': job,
        'form': form,
        'applicants': applicants,
        'applied': applied,
        'bookmarked': bookmarked,
    }

    return render(request, template, context)


@login_required
def job_update(request, pk):
    """
    Returns the form page for updating a job.

    Template: ``jobs/job_form.html``
    Context:
        form
            JobForm object
        job
            job object 
    """
    job = get_object_or_404(job, pk=pk)
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect(job)
    else:
        form = JobForm(instance=job)

    template_name= 'jobs/job_update.html'
    context = {
        'form': form,
        'job': job,
    }

    return render(request, template_name, context)


@login_required
def job_delete(request, pk):
    """
    Returns a job delete confirmation page.

    Templates: ``jobs/job_delete_confirm.html``
    Context:
        job
            job object
    """
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.is_active = False
        job.save()
        return redirect('/')

    template_name= 'jobs/job_delete_confirm.html'
    context = {
        'job': job,
    }

    return render(request, template_name, context)


def resumes(request):
    # applicants = Applicant.objects.all()

    template = 'resumes.html'
    context = {
        # 'applicants': applicants,
    }

    return render(request, template, context)


def resume_detail(request, username):
    # user = get_object_or_404(User, username=username)
    # resume = get_object_or_404(Applicant, user=user)

    template = 'resume_detail.html'
    context = {
        # 'user': user,
        # 'resume': resume,
    }

    return render(request, template, context)


@login_required
def add_bookmark(request, id):
    job = get_object_or_404(Job, id=id)
    if job.bookmarks.filter(id=request.user.employee.id).exists():
        job.bookmarks.remove(request.user.employee)
    else:
        job.bookmarks.add(request.user.employee)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
