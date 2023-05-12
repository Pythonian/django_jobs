from django.db import models
from django.conf import settings


class Testimonial(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
