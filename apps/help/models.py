from django.db import models


class Category(models.Model):

    name = models.CharField()
    slug = models.SlugField()
    description = models.CharField()
    icon = models.CharField()
