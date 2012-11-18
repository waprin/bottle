from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail

class Command(BaseCommand):

    def handle(self, *args, **options):
        send_mail('great sub', 'this is the message', 'from@example.com', ['waprin@gmail.com'], fail_silently=False)
