from django.urls import path

from .views import home, companies, company_detail, dashboard, resumes

app_name = 'core'

urlpatterns = [
    path('companies/', companies, name='companies'),
    path('resumes/', resumes, name='resumes'),
    path('company/<slug:slug>/', company_detail, name='company_detail'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', home, name='home'),
]
