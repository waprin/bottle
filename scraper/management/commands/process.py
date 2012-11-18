from django.core.management.base import BaseCommand, CommandError
from scraper.models import Ad

class Command(BaseCommand):

    def handle(self, *args, **options):
                    #Ad.objects.get(clid=cl_id)
        self.stdout.write("processing\n")

                 
