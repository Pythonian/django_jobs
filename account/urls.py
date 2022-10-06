from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
     path('logout/',
          auth_views.LogoutView.as_view(), name='logout'),
     path('login/',
          auth_views.LoginView.as_view(
               redirect_authenticated_user=True), name='login'),

     path('signup/choice/', views.signup_choice, name='signup_choice'),
     path('signup/seeker/', views.signup, name='signup'),
     path('signup/employer/', views.signup_employer, name='signup_employer'),
]
