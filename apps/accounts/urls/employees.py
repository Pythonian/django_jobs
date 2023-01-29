from django.urls import path

from ..views import employees

app_name = 'employees'

urlpatterns = [
    path('dashboard/', employees.employee_dashboard, name='dashboard'),
    path('profile/', employees.employee_account, name='account'),
    path('jobs/', employees.employee_jobs, name='jobs'),
    path('messages/', employees.employee_messages, name='messages'),
    path('resume/', employees.employee_resume, name='resume'),
    path('bookmarks/', employees.employee_bookmarks, name='bookmarks'),

    path('resume/<int:id>/', employees.resume_detail, name='resume_detail'),
]
