from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='list'),
    path('new/', views.job_create, name='create'),
    path('<slug:slug>/', views.job_detail, name='detail'),
    path('bookmark/<int:id>/', views.add_bookmark, name='add_bookmark'),
]
