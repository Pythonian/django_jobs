from django.urls import path

from .views import index, article, category, faq, search

app_name = "help"

urlpatterns = [
    path("faq/", faq, name="faq"),
    path("search/", search, name="search"),
    path("<slug:slug>/", category, name="category"),
    path("<slug:category_slug>/<slug:article_slug>/", article, name="article"),
    path("", index, name="index"),
]
