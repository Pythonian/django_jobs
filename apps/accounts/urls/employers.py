from django.urls import path

from ..views import employers

app_name = 'employers'

urlpatterns = [
    path('company/profile/', employers.company_account, name='company_account'),
    path('company/jobs/', employers.company_jobs, name='company_jobs'),
    path('company/candidates/', employers.company_candidates, name='company_candidates'),
]
