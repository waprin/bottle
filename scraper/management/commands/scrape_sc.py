from django.core.management.base import BaseCommand, CommandError
from scraper.models import CrushAd
import urllib2
from bs4 import BeautifulSoup
import re

class Command(BaseCommand):

    def handle(self, *args, **options):
        root_url = "http://ny.subwaycrush.com/"

        self.stdout.write("making first request\n")
        response = urllib2.urlopen(root_url)
        html = response.read()
        pool = BeautifulSoup(html)

        self.stdout.write("first request sucessful\n")
        results = pool.findAll('div', attrs={'class' : 'post'})

        for result in results:
            link_tag = result.findAll('a')
            ad_url = link_tag[1]["href"]
            final_url = root_url + ad_url
            
            try:
                x = CrushAd.objects.filter(sc_id=ad_url)[:1]
                if len(x) > 0: 
                    self.stdout.write("crush ad already exists\n")
                    continue
            except CrushAd.DoesNotExist:
                pass
            self.stdout.write("new crush ad, querying now\n")

            ad_response = urllib2.urlopen(final_url)
            ad_html = ad_response.read()
            ad_pool = BeautifulSoup(ad_html)

            post = ad_pool.find('div', attrs = {'class' : 'post-single'})
            title_tag = post.find('h2')
            title = title_tag.string

            content = ad_pool.find('div', attrs = {'id' : 'post_description' })
            text = content.findAll(text=True)
            ad_content = ''.join(text)

            ad = CrushAd(city="NY", title=title, content=ad_content, sc_id=ad_url, processed=False) 
            ad.save()

