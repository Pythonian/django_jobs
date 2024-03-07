from django.urls import path

from .views import home, companies, company_detail, dashboard, resumes, AboutView, PolicyView, post, contact

app_name = "core"

urlpatterns = [
    path("companies/", companies, name="companies"),
    path("contact/", contact, name="contact"),
    path("resumes/", resumes, name="resumes"),
    path("company/<slug:slug>/", company_detail, name="company_detail"),
    path("dashboard/", dashboard, name="dashboard"),
    path("policy/", PolicyView.as_view(), name="policy"),
    path("about/", AboutView.as_view(), name="about"),
    path("post/", post, name="post"),
    path("", home, name="home"),
]
