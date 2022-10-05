from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('logout/',
         auth_views.LogoutView.as_view(), name='logout'),
    path('login/',
         auth_views.LoginView.as_view(
             redirect_authenticated_user=True), name='login'),

     path('signup/', views.signup, name='signup'),
]
