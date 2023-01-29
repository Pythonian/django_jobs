"""blue_jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import home, companies, company_detail, dashboard, resumes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.accounts.urls.auth', namespace='auth')),
    path('account/', include('apps.accounts.urls')),
    path('jobs/', include('apps.jobs.urls', namespace='jobs')),
    path('companies/', companies, name='companies'),
    path('resumes/', resumes, name='resumes'),
    path('company/<slug:slug>/', company_detail, name='company_detail'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Blue Jobs Admin'
admin.site.index_title = 'Blue Collar Jobs Admin'
admin.site.site_title = 'Blue Collar Jobs Administration'
