from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    name = models.CharField(
        _("name"),
        max_length=30,
        db_index=True,
    )
    slug = models.SlugField(
        _("slug"),
        max_length=30,
    )
    description = models.CharField(
        _("description"),
        max_length=100,
    )
    icon = models.CharField(
        _("fontawesome icon"),
        max_length=20,
    )

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        """String representation of the category instance."""
        return self.name

    def get_absolute_url(self):
        return reverse("help:category", kwargs={"slug": self.slug})

    def get_article_count(self):
        return Article.objects.filter(category=self).count()


class Article(models.Model):
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name=_("category"),
        related_name=_("articles"),
        help_text=_("Category linked to this Help Article."),
    )
    title = models.CharField(
        _("title"),
        max_length=255,
        unique=True,
        help_text=_("Title of the Help Article."),
    )
    slug = models.SlugField(
        _("slug"),
        max_length=255,
        help_text=_("URL slug parameter"),
    )
    content = models.TextField(
        _("content"),
        help_text=_("Content of the Article."),
    )

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "help:article",
            kwargs={
                "article_slug": self.slug,
                "category_slug": self.category.slug,
            },
        )


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(
        _("question"),
        max_length=255,
        unique=True,
    )
    answer = models.TextField(
        _("answer"),
    )

    class Meta:
        verbose_name = _("frequently asked question")
        verbose_name_plural = _("frequently asked questions")

    def __str__(self):
        return self.question
