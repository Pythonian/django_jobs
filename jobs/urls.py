from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job_list, name='job_list'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('companies/', views.companies, name='companies'),
    path('company/<int:id>/', views.company_detail, name='company_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('resumes/', views.resumes, name='resumes'),
    path('resume/<str:username>/', views.resume_detail, name='resume_detail'),
    # path('create-job/', views.job_create, name='create_job'),
    path('', views.home, name='home'),
]
