from django.shortcuts import render

from jobs.models import Job


def home(request):
    jobs = Job.active.all()[:4]
    # companies = Company.objects.all()
    # resumes = Applicant.objects.all()

    template = 'home.html'
    context = {
        'jobs': jobs,
        # 'companies': companies,
        # 'resumes': resumes,
    }

    return render(request, template, context)
