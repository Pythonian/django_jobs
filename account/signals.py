from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Company, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_company:
            Company.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_company:
        instance.company.save()
