from django.urls import path

from ..views import employees

app_name = 'employees'

urlpatterns = [
    path('employee/dashboard/', employees.employee_dashboard, name='employee_dashboard'),
    path('employee/profile/', employees.employee_account, name='employee_account'),
    path('employee/jobs/', employees.employee_jobs, name='employee_jobs'),
    path('employee/messages/', employees.employee_messages, name='employee_messages'),
    path('employee/resume/', employees.employee_resume, name='employee_resume'),
    path('employee/bookmarks/', employees.employee_bookmarks, name='employee_bookmarks'),

    path('resume/<int:id>/', employees.resume_detail, name='resume_detail'),
]
