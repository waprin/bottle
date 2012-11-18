from django.core.management.base import BaseCommand, CommandError
from scraper.models import CraigslistAd
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
                ad_url = link["href"]
                self.stdout.write("handing ad %s \n" % ad_url) 

                cl_id_match = p.search(ad_url)
                cl_id = cl_id_match.group(1)

                try:
                    CraigslistAd.objects.get(cl_id=cl_id)
                    self.stdout.write("craigslist ad already exists\n")
                    continue
                except CraigslistAd.DoesNotExist:
                    pass
                self.stdout.write("new ad, querying now\n")

                ad_response = urllib2.urlopen(ad_url)
                ad_html = ad_response.read()
                ad_pool = BeautifulSoup(ad_html)

                title = ad_pool.find('h2', attrs={'class' : 'postingtitle'}).string
                content = ad_pool.find('div', attrs={'id' : 'userbody'}).contents
               
                self.stdout.write("saving ad with title %s " % title)
                ad = CraigslistAd(title=title, content=content,url=ad_url, cl_id = cl_id, processed=False, city="NY")
                ad.save()
                break
            break
