from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.core.mail import send_mail


class Command(BaseCommand):
    help = 'Send an email to all registered users'

    def handle(self, *args, **kwargs):
        subject = 'Important message from your site administrator'
        message = 'Dear user,\n\nThis is an important message from the site administrator.\n\nBest regards,\nSite administrator'
        from_email = 'noreply@yourdomain.com'
        recipient_list = [user.email for user in User.objects.all()]
        send_mail(subject, message, from_email, recipient_list)
        self.stdout.write(self.style.SUCCESS(f'Emails sent to {len(recipient_list)} users'))
