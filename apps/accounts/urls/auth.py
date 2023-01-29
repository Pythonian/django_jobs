from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from ..forms import UserLoginForm
from apps.accounts.views.auth import (CustomLogoutView, CustomPasswordChangeView,
                    signup_choice, signup_employee, signup_employer, activate)

app_name = 'auth'

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
             success_url=reverse_lazy('auth:password_reset_done')),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             success_url=reverse_lazy('auth:password_reset_complete')),
         name='password_reset_confirm'),
    path('password_reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # password change
    path('password_change/', CustomPasswordChangeView.as_view(),
         name='password_change'),

]
