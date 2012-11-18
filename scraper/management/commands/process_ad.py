from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from scraper.models import CrushAd
from describe.models import Description
import re
import smtplib


class Command(BaseCommand):

    def get_hair_color(self, content):
        p = re.compile(r'(blonde|blond|red|brown|grey).{0,10}?hair') 
        m = p.search(content)
        if m is None:
            return None
        color = m.group(1).lower()
        if color == "blond":
            color = "blonde"
        return color

    def get_hair_length(self, content):
        p = re.compile(r'(long|short|medium length).{0,10}?hair') 
        m = p.search(content)
        if m is None:
            return None
        length = m.group(1).lower()
        if length == "medium length":
            return "medium"
        return length

    def get_gender(self, content):
        return None

    def get_eye_color(self, content):
        p = re.compile(r'(brown|blue|green|hazel).{0,10}?hair')
        m = p.search(content)
        if m is None:
            return None 
        return m.group(1).lower()

    def get_race(self, content):
        return None

    def get_tone(self, content):
        return None

    def get_age(self, content):
        return None

    def get_height(self, content):
        return None
        
    def handle(self, *args, **options):
        rooturl="ny.subwaycrush.com"
        ads = CrushAd.objects.filter(processed=False)
        for ad in ads:
            self.stdout.write("processing ad %s\n" % ad.title)
            ad_description = self.process_ad(ad)

            people = Description.objects.all()
            for person in people:
                self.stdout.write("comparing it to user %s\n" % person.email)
                self.match_ad(ad_description, person, ad.title, rooturl + ad.sc_id)

            ad.processed = True
            ad.save()

    def match_ad(self, ad, person, title, url):
        points = 0
        if person.hair_color == ad.hair_color:
            self.stdout.write("matched hair color\n")
            points += 1
        else:
            self.stdout.write("person hair color was %s \n" % person.hair_color)
            self.stdout.write("ad hair color was %s \n" % ad.hair_color)
        if person.hair_length == ad.hair_length:
            self.stdout.write("matched hair length\n")
            points += 1
        if person.gender == ad.gender:
            self.stdout.write("matched gender\n")
            points += 1
        if person.eyes == ad.eyes:
            self.stdout.write("matched eye color\n")
            points += 1
        else:
            self.stdout.write("person eye color was %s \n" %ad.eyes)
            self.stdout.write("ad eye color was %s \n" % ad.eyes)
        if person.race == ad.race:
            self.stdout.write("matched race\n")
            points += 1
        if person.tone == ad.tone:
            self.stdout.write("matched tone\n")
            points += 1
        if person.height == ad.height:
            self.stdout.write("matched height\n")
            points += 1
        self.stdout.write("total points\n") 

        if points > 1:
            self.stdout.write("sending email\n")
            me = "cupid@subwaycrushed.com"
            you = person.email

            subject = 'You\'ve been Subway Crushed!'
            text = "You must be looking good! This ad may be about you! %s" % url 
            html = """\
            <html>
              <head></head>
              <body>
                You must be looking good! This ad may be about you!
                <br>
                    <a href="%s">%s</a>
              </body>
            </html>
            """ % (url, title)
            msg = EmailMultiAlternatives(subject, text, me, [you])
            msg.attach_alternative(html, "text/html")
            msg.send()
            #send_mail(, '<br/><a href="%s">%s</a>' % (url, title), 'from@example.com',[person.email], fail_silently=False)   
        else:
            self.stdout.write("didnt earn enough points to match\n")
    
    def process_ad(self, ad):
        points = 0

        hair_color = self.get_hair_color(ad.content)
        hair_length = self.get_hair_color(ad.content)
        gender = self.get_gender(ad.content)
        eyes = self.get_eye_color(ad.content)
        race = self.get_race(ad.content)
        tone = self.get_tone(ad.content)
        height = self.get_height(ad.content)
        age = self.get_age(ad.content)

        ad_description = Description(hair_color=hair_color, hair_length=hair_length, gender=gender, height=height,age=age,tone=tone,eyes=eyes,race=race)
        return ad_description

