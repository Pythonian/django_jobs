"""django_jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('jobs/', include('jobs.urls', namespace='jobs')),
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
