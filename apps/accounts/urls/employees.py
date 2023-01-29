from django.urls import path

from ..views import (employee_account, employee_jobs, employee_resume,
                    signup_employee, employee_bookmarks, employee_dashboard,
                    employee_messages, resume_detail)

urlpatterns = [
    path('signup/employee/', signup_employee, name='signup_employee'),

    path('employee/dashboard/', employee_dashboard, name='employee_dashboard'),
    path('employee/profile/', employee_account, name='employee_account'),
    path('employee/jobs/', employee_jobs, name='employee_jobs'),
    path('employee/messages/', employee_messages, name='employee_messages'),
    path('employee/resume/', employee_resume, name='employee_resume'),
    path('employee/bookmarks/', employee_bookmarks, name='employee_bookmarks'),

    path('resume/<int:id>/', resume_detail, name='resume_detail'),
]
