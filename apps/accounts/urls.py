from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from .forms import UserLoginForm
from .views import (CustomLogoutView, CustomPasswordChangeView,
                    company_account, company_candidates, company_jobs,
                    employee_account, employee_jobs, signup_choice, employee_resume,
                    signup_employee, employee_bookmarks, signup_employer, activate, employee_dashboard,
                    employee_messages, resume_detail)

urlpatterns = [
     path('logout/', CustomLogoutView.as_view(), name='logout'),
     path('login/',
          auth_views.LoginView.as_view(
               redirect_authenticated_user=True, authentication_form=UserLoginForm), name='login'),

     path('signup/choice/', signup_choice, name='signup_choice'),
     path('signup/employee/', signup_employee, name='signup_employee'),
     path('signup/employer/', signup_employer, name='signup_employer'),

     path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),

     # password reset with email
     path('password_reset/',
          auth_views.PasswordResetView.as_view(
               success_url=reverse_lazy('password_reset_done')),
          name='password_reset'),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
          name='password_reset_done'),
     path('password_reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(
               success_url=reverse_lazy('password_reset_complete')),
          name='password_reset_confirm'),
     path('password_reset/complete/',
          auth_views.PasswordResetCompleteView.as_view(),
          name='password_reset_complete'),

     # password change
     path('password_change/', CustomPasswordChangeView.as_view(),
          name='password_change'),

     path('employee/dashboard/', employee_dashboard, name='employee_dashboard'),
     path('employee/profile/', employee_account, name='employee_account'),
     path('employee/jobs/', employee_jobs, name='employee_jobs'),
     path('employee/messages/', employee_messages, name='employee_messages'),
     path('employee/resume/', employee_resume, name='employee_resume'),
     path('employee/bookmarks/', employee_bookmarks, name='employee_bookmarks'),
     
     path('resume/<int:id>/', resume_detail, name='resume_detail'),
     
     path('company/profile/', company_account, name='company_account'),
     path('company/jobs/', company_jobs, name='company_jobs'),
     path('company/candidates/', company_candidates, name='company_candidates'),
]
