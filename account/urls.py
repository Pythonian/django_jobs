from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from .views import signup_employee, signup_choice, signup_employer, signup_employee, company_account, company_jobs, company_candidates, CustomPasswordChangeView, employee_account
from .forms import UserLoginForm

urlpatterns = [
     path('logout/',
          auth_views.LogoutView.as_view(), name='logout'),
     path('login/',
          auth_views.LoginView.as_view(
               redirect_authenticated_user=True, authentication_form=UserLoginForm), name='login'),

     path('signup/choice/', signup_choice, name='signup_choice'),
     path('signup/employee/', signup_employee, name='signup_employee'),
     path('signup/employer/', signup_employer, name='signup_employer'),

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

     path('employee/profile/', employee_account, name='employee_account'),
     
     path('company/profile/', company_account, name='company_account'),
     path('company/jobs/', company_jobs, name='company_jobs'),
     path('company/candidates/', company_candidates, name='company_candidates'),
]
