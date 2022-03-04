from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
#     path('create-job/', views.job_create, name='create_job'),
#     path('<str:slug>/', views.job_detail, name='job_detail'),
]
