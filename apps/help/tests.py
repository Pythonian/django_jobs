# from django.test import TestCase
# from django.urls import reverse
# from django.utils.text import slugify

# from .models import Category
# from apps.help.management.commands.populate_categories import Command as PopulateCategoriesCommand


# class CategoryModelTests(TestCase):

#     def setUp(self):
#         self.category_data = {
#             "name": "Test Category",
#             "slug": "test-category",
#             "description": "This is a test category.",
#             "icon": "test-icon",
#         }

#     def test_category_creation(self):
#         category = Category.objects.create(**self.category_data)
#         self.assertEqual(category.name, "Test Category")
#         self.assertEqual(category.slug, "test-category")
#         self.assertEqual(category.description, "This is a test category.")
#         self.assertEqual(category.icon, "test-icon")

#     def test_get_absolute_url(self):
#         category = Category.objects.create(**self.category_data)
#         url = reverse("help:category", kwargs={"slug": category.slug})
#         self.assertEqual(category.get_absolute_url(), url)

#     def test_get_article_count(self):
#         category = Category.objects.create(**self.category_data)
#         # Assuming you have an 'Article' model, you need to import it
#         from apps.help.models import Article

#         Article.objects.create(category=category, title="Test Article", content="Article content")
#         self.assertEqual(category.get_article_count(), 1)


# class PopulateCategoriesCommandTests(TestCase):

#     def test_populate_categories_command(self):
#         command = PopulateCategoriesCommand()
#         command.handle()

#         # Check if the categories have been created
#         self.assertEqual(Category.objects.count(), 6)

#         # Check if the icon field is chosen from the provided list
#         icons = [category.icon for category in Category.objects.all()]
#         self.assertIn(icons[0], ["user", "cog", "file", "question", "lock", "chart-bar"])

#         # Add more assertions as needed based on your specific requirements
