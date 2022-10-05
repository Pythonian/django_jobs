from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='list'),
    path('new/', views.job_create, name='create'),
    path('<slug:slug>/', views.job_detail, name='detail'),
    path('companies/', views.companies, name='companies'),
    path('company/<int:id>/', views.company_detail, name='company_detail'),
    path('resumes/', views.resumes, name='resumes'),
    path('resume/<str:username>/', views.resume_detail, name='resume_detail'),
]
