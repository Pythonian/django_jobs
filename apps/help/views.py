from django.shortcuts import render, get_object_or_404

from .models import Article, Category, FrequentlyAskedQuestion


def index(request):

    categories = Category.objects.all()

    template = "help/index.html"
    context = {
        "categories": categories,
    }

    return render(request, template, context)


def article(request, category_slug, article_slug):

    category = get_object_or_404(Category, slug=category_slug)
    article = get_object_or_404(Article, category=category, slug=article_slug)
    related_categories = Category.objects.exclude(articles__isnull=True).order_by("?")[:3]

    template = "help/article.html"
    context = {
        "article": article,
        "category": category,
        "related_categories": related_categories,
    }

    return render(request, template, context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category)
    random_categories = Category.objects.exclude(id=category.id).exclude(articles__isnull=True).order_by("?")[:3]

    template = "help/category.html"
    context = {
        "category": category,
        "articles": articles,
        "random_categories": random_categories,
    }

    return render(request, template, context)


def faq(request):

    questions = FrequentlyAskedQuestion.objects.all()

    template = "help/faq.html"
    context = {
        "questions": questions,
    }

    return render(request, template, context)
