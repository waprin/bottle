from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from scraper.models import CrushAd
import re

class Command(BaseCommand):

    def get_hair_color(self, content):
        p = re.compile(r'(blonde|blond|red|brown|grey).{0,10}?hair') 
        m = p.search(content)
        return None

    def get_hair_length(self, content):
        p = re.compile(r'(long|short|medium length).{0,10}?hair') 
        return None

    def get_gender(self, content):
        return None

    def get_eye_color(self, content):
        p = re.compile(r'(brown|blue|green|hazel).{0,10)?hair')
        return None 

    def get_race(self, content):
        return None

    def get_tone(self, content):
        return None

    def get_age(self, content):
        return None

    def get_height(self, content):
        return None
        
    def handle(self, *args, **options):
        self.init_res()
        
        CrushAd.objects.get(processed=False)
        ad = CrushAd.objects.filter(processed=False)[:1][0]

        points = 0

        hair_color = self.get_hair_color(ad.content)
        hair_length = self.get_hair_color(ad.content)
        gender = self.get_gender(ad.content)
        eye_color = self.get_eye_color(ad.content)
        race = self.get_race(ad.content)
        tone = self.get_tone(ad.content)
        height = self.get_height(ad.content)

        if hair_color == ad.hair_color:
            self.stdout.write("matched hair color\n")
            points += 1
        if hair_length == ad.hair_length:
            self.stdout.write("matched hair length\n")
            points += 1
        if gender == ad.gender:
            self.stdout.write("matched gender\n")
            points += 1
        if eye_color == ad.eye_color:
            self.stdout.write("matched eye color\n")
            points += 1
        if race == ad.race:
            self.stdout.write("matched race\n")
            points += 1
        if tone == ad.tone:
            self.stdout.write("matched tone\n")
            points += 1
        if height == ad.height:
            self.stdout.write("matched height\n")
            points += 1
        
        self.stdout.write("total points\n") 

        send_mail('great sub', 'this is the message', 'from@example.com', ['waprin@gmail.com'], fail_silently=False)
