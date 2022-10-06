from django.shortcuts import render

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
