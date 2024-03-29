from django.contrib import admin

from .models import Article, Category, FrequentlyAskedQuestion, Testimonial


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "category"]
    list_filter = ["category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "description", "get_article_count"]
    search_fields = ["name", "description"]

    def get_article_count(self, obj):
        return obj.get_article_count()

    get_article_count.short_description = "No. of Articles"


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ["question"]
    search_fields = ["question", "answer"]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["fullname", "rating"]
    search_fields = ["fullname", "content"]
    list_filter = ["rating"]
