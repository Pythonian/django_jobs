from django.urls import path

from ..views import company_account, company_candidates, company_jobs

app_name = 'employers'

urlpatterns = [
    path('company/profile/', company_account, name='company_account'),
    path('company/jobs/', company_jobs, name='company_jobs'),
    path('company/candidates/', company_candidates, name='company_candidates'),
]
