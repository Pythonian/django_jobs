from datetime import timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.db.models import Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import JobForm, ApplicationForm
from .models import Job, State, JobType, Category
from apps.core.utils import mk_paginator
from apps.accounts.decorators import employer_required
import random


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = "jobs/form.html"
    fields = ("title", "description")

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)


@login_required
@employer_required
def job_create(request):
    """
    Returns the form page for creating a Job.

    :param request: A request object used to generate the HttpResponse

    Template: ``jobs/form.html``
    Context:
        form (JobForm)
    """

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company
            job.save()
            messages.success(request, "Job details saved successfully.")
            return redirect(job)
        else:
            messages.error(request, "Error: Invalid form submission.")
    else:
        form = JobForm()

    template = "jobs/form.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def job_list(request):
    """
    View that returns the page for viewing all jobs.

    :param request: A request object used to generate the HttpResponse

    Template: ``jobs/list.html``
    Context:
        jobs:
            A list of active job objects
        jobs_last_24_hours:
            The number of jobs created in the last 24 hours
        jobs_last_7_days:
            The number of jobs created in the last 7 days
        jobs_last_30_days:
            The number of jobs created in the last 30 days
        states:
            A list of all the state objects
        categories:
            A list of all the category objects
        job_types:
            A list of all the job type objects
        salary_mode_counts:
            A dictionary containing salary mode as key and job count as value
        genders:
            A list of tuples containing all the gender choices for a job
    """

    jobs = Job.active.all()
    categories = Category.objects.all()
    states = State.objects.all()
    job_types = JobType.objects.all()
    genders = Job.GenderStatus.choices

    # create a list of salary modes by extracting the first element of each tuple
    # in the choices attribute of the SalarySchedule field in the Job model
    salary_modes = [mode[0] for mode in Job.SalarySchedule.choices]
    # maps each salary mode to a count of 0 in the dictionary
    salary_mode_counts = {mode: 0 for mode in salary_modes}
    # counts the number of Job objects for each salary mode
    salary_mode_counts_query = Job.active.values("salary_mode").annotate(jobs_count=Count("id"))
    # updates the count of the corresponding salary mode in the dictionary
    for smc in salary_mode_counts_query:
        salary_mode_counts[smc.get("salary_mode")] = smc.get("jobs_count")

    last_24_hours = timezone.now() - timezone.timedelta(hours=24)
    jobs_last_24_hours = jobs.filter(created__gte=last_24_hours).count()

    last_7_days = timezone.now() - timezone.timedelta(days=7)
    jobs_last_7_days = jobs.filter(created__gte=last_7_days).count()

    last_30_days = timezone.now() - timezone.timedelta(days=30)
    jobs_last_30_days = jobs.filter(created__gte=last_30_days).count()

    title = request.GET.get("title", None)
    category = request.GET.get("category", None)
    state = request.GET.get("state", None)
    gender = request.GET.get("gender", None)
    job_type = request.GET.get("job_type", None)
    salary_mode = request.GET.get("salary_mode", None)
    posted = request.GET.get("posted", None)

    if title:
        jobs = jobs.filter(title__icontains=title)
    if category:
        jobs = jobs.filter(category__name=category)
    if state:
        jobs = jobs.filter(state__name=state)
    if gender:
        jobs = jobs.filter(gender=gender)
    if job_type:
        jobs = jobs.filter(jobtype__name=job_type)
    if salary_mode:
        jobs = jobs.filter(salary_mode=salary_mode)
    if posted:
        if posted == "24h":
            jobs = jobs.filter(created__gte=timezone.now() - timedelta(hours=24))
        elif posted == "7d":
            jobs = jobs.filter(created__gte=timezone.now() - timedelta(days=7))
        elif posted == "30d":
            jobs = jobs.filter(created__gte=timezone.now() - timedelta(days=30))

    # Paginate the jobs queryset
    jobs = mk_paginator(request, jobs, 6)

    template = "jobs/list.html"
    context = {
        "jobs": jobs,
        "states": states,
        "job_types": job_types,
        "categories": categories,
        "genders": genders,
        "jobs_last_24_hours": jobs_last_24_hours,
        "jobs_last_7_days": jobs_last_7_days,
        "jobs_last_30_days": jobs_last_30_days,
        "salary_mode_counts": salary_mode_counts,
    }

    return render(request, template, context)


def job_detail(request, slug):
    """
    Returns the detail page of a Job.

    :param request: A request object used to generate the HttpResponse
    :param slug: Identifies the specific job being requested for

    Template: ``jobs/detail.html``
    Context:
        job:
            A Job object instance
        form:
            An instance of the ApplicationForm
        applicants:
            An integer representing the number of applicants for the job
        applied:
            A boolean indicating whether the current user has applied for the job
        bookmarked:
            A boolean indicating whether the current user has bookmarked the job
        similar_jobs_by_category:
            A QuerySet of 4 similar jobs based on category
        related_jobs_by_company:
            A QuerySet of 4 related jobs based on company
        related_jobs_by_job_type:
            A QuerySet of 4 related jobs based on job type
    """

    job = get_object_or_404(Job, slug=slug)

    # Create a session key for a user
    session_key = "viewed_job_{}".format(job.pk)
    if not request.session.get(session_key, False):
        job.impressions += 1
        job.save()
        request.session[session_key] = True

    is_employee = request.user.is_authenticated and request.user.is_employee
    applied = job.applicants.filter(id=request.user.employee.id).exists() if is_employee else False
    bookmarked = job.bookmarks.filter(id=request.user.employee.id).exists() if is_employee else False

    similar_jobs_by_category = Job.active.filter(category=job.category).exclude(id=job.id)[:4]
    related_jobs_by_company = Job.active.filter(company=job.company).exclude(id=job.id)[:4]
    related_jobs_by_job_type = Job.active.filter(jobtype=job.jobtype).exclude(id=job.id)[:4]

    applicants = job.applicants.count()

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            if is_employee:
                application = form.save(commit=False)
                application.job = job
                application.applicant = request.user.employee
                application.save()
                job.applicants.add(request.user.employee)
                messages.success(request, "Your application request was sent.")
                return redirect(job)
            else:
                messages.error(request, "You must be an employee to apply for this job.")
    else:
        form = ApplicationForm()

    template = "jobs/detail.html"
    context = {
        "job": job,
        "form": form,
        "applicants": applicants,
        "applied": applied,
        "bookmarked": bookmarked,
        "similar_jobs_by_category": similar_jobs_by_category,
        "related_jobs_by_company": related_jobs_by_company,
        "related_jobs_by_job_type": related_jobs_by_job_type,
    }

    return render(request, template, context)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ("title", "description")
    template_name = "jobs/form.html"

    def test_func(self):
        obj = self.get_object()
        return obj.company == self.request.user.company


@login_required
def job_update(request, pk):
    """
    Returns the form page for updating a job.

    Template: ``jobs/form.html``
    Context:
        form
            JobForm object
        job
            job object
    """
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect(job)
    else:
        form = JobForm(instance=job)

    template_name = "jobs/form.html"
    context = {
        "form": form,
        "job": job,
    }

    return render(request, template_name, context)


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    template_name = "jobs/delete_confirm.html"
    success_url = reverse_lazy("jobs:list")

    def test_func(self):
        obj = self.get_object()
        return obj.company == self.request.user.company


@login_required
def job_delete(request, pk):
    """
    Returns a job delete confirmation page.

    Templates: ``jobs/delete_confirm.html``
    Context:
        job
            job object
    """
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        # job.is_active = False
        job.save()
        return redirect("employers:jobs")

    template_name = "jobs/delete_confirm.html"
    context = {
        "job": job,
    }

    return render(request, template_name, context)


@login_required
def add_bookmark(request, id):
    job = get_object_or_404(Job, id=id)
    if job.bookmarks.filter(id=request.user.employee.id).exists():
        job.bookmarks.remove(request.user.employee)
        messages.success(request, "Bookmark removed")
    else:
        job.bookmarks.add(request.user.employee)
        messages.success(request, "Bookmark added")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
