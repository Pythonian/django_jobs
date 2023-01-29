from django.urls import path

from ..views import employers

app_name = 'employers'

urlpatterns = [
    path('company/profile/', employers.company_account, name='account'),
    path('company/jobs/', employers.company_jobs, name='jobs'),
    path('company/candidates/', employers.company_candidates, name='candidates'),
]
