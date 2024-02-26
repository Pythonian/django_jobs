from django.shortcuts import render, get_object_or_404

from .models import Article, Category


def index(request):

    categories = Category.objects.all()

    template = "help/index.html"
    context = {
        "categories": categories,
    }

    return render(request, template, context)


def article(request, category_slug, article_slug):

    template = "help/article.html"
    context = {}

    return render(request, template, context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category)
    random_categories = Category.objects.exclude(id=category.id).order_by("?")[:3]

    template = "help/category.html"
    context = {
        "category": category,
        "articles": articles,
        "random_categories": random_categories,
    }

    return render(request, template, context)
