from django.core.management.base import BaseCommand, CommandError
from scraper.models import Ad
import urllib2
from bs4 import BeautifulSoup
import re

class Command(BaseCommand):

    def handle(self, *args, **options):
        listings_url = 'http://newyork.craigslist.org/search/mis?query=w4m'
        listings_response = urllib2.urlopen(listings_url)
        listings_html = listings_response.read()

        pool = BeautifulSoup(listings_html)
        ad_rows = pool.findAll('p', attrs={'class' : 'row'})

        for ad_row in ad_rows:
            for link in ad_row.findAll('a'):
                # TODO - global init to compile regex
                p = re.compile(r'(\d+).html')
                ad = link["href"]
                self.stdout.write("handing ad %s \n" % ad) 

                cl_id_match = p.search(ad)
                cl_id = cl_id_match.group(1)

                try:
                    Ad.objects.get(clid=cl_id)
                    self.stdout.write("ad already exists\n")
                    continue
                except Ad.DoesNotExist:
                    pass
                self.stdout.write("new ad, querying now\n")

                ad_response = urllib2.urlopen(ad)
                ad_html = ad_response.read()
                ad_pool = BeautifulSoup(ad_html)

                title = ad_pool.find('h2', attrs={'class' : 'postingtitle'})
                content = ad_pool.find('div', attrs={'id' :
