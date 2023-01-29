"""bluejobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.accounts.urls.auth', namespace='auth')),
    path('employees/', include('apps.accounts.urls.employees', namespace='employees')),
    path('employers/', include('apps.accounts.urls.employers', namespace='employers')),
    path('jobs/', include('apps.jobs.urls', namespace='jobs')),
    path('', include('apps.core.urls', namespace='core')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

admin.site.site_header = 'Blue Jobs Admin'
admin.site.index_title = 'Blue Collar Jobs Admin'
admin.site.site_title = 'Blue Collar Jobs Administration'
