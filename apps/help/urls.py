from django.urls import path

from .views import index, article, category

app_name = "help"

urlpatterns = [
    path("", index, name="index"),
    path("<slug:slug>/", category, name="category"),
    path("<slug:category_slug>/<slug:article_slug>/", article, name="article"),
]
