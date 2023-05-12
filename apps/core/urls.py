from django.urls import path

from .views import home, companies, company_detail, dashboard, resumes, help_center, help_article, faq, about, policy, help_category, post, contact

app_name = 'core'

urlpatterns = [
    path('companies/', companies, name='companies'),
    path('contact/', contact, name='contact'),
    path('resumes/', resumes, name='resumes'),
    path('company/<slug:slug>/', company_detail, name='company_detail'),
    path('dashboard/', dashboard, name='dashboard'),
    path('faq/', faq, name='faq'),
    path('policy/', policy, name='policy'),
    path('about/', about, name='about'),
    path('post/', post, name='post'),
    path('help/', help_center, name='help_center'),
    path('help/category/', help_category, name='help_category'),
    path('help/category/article/', help_article, name='help_article'),
    path('', home, name='home'),
]
