from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobForm
from .models import Job
from .utils import mk_paginator, is_valid_query_paramter


@login_required
def job_create(request):
    """
    Returns the form page for creating a Lead.

    Template: ``leads/lead_form.html``
    Context:
        form
            LeadForm object
    """
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user
            job.save()
            messages.success(request, "Job details saved.")
            return redirect(job)
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
    jobs = mk_paginator(request, jobs, 2)

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
    # applicants = job.applications.all()

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

    template = 'job_detail.html'
    context = {
        'job': job,
        # 'applicants': applicants,
    }

    return render(request, template, context)


@login_required
# def lead_update(request, pk):
#     """
#     Returns the form page for updating a Lead.

#     Template: ``leads/lead_form.html``
#     Context:
#         form
#             LeadForm object
#         lead
#             Lead object 
#     """
#     lead = get_object_or_404(Lead, pk=pk)
#     if request.method == 'POST':
#         form = LeadForm(request.POST, request.FILES, instance=lead)
#         if form.is_valid():
#             form.save()
#             # return redirect(new_lead.get_absolute_url())
#             return redirect('/')
#     else:
#         form = LeadForm(instance=lead)

#     template_name= 'leads/lead_update.html'
#     context = {
#         'form': form,
#         'lead': lead,
#     }

#     return render(request, template_name, context)


# @login_required
# def lead_delete(request, pk):
#     """
#     Returns a lead delete confirmation page.

#     Templates: ``leads/lead_delete_confirm.html``
#     Context:
#         lead
#             Lead object
#     """
#     lead = get_object_or_404(Lead, pk=pk)
#     if request.method == 'POST':
#         lead.is_active = False
#         lead.save()
#         return redirect('/')

#     template_name= 'leads/lead_delete_confirm.html'
#     context = {
#         'lead': lead,
#     }

#     return render(request, template_name, context)


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
