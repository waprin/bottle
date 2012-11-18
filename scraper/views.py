# Create your views here.

from django.http import HttpResponse
from scaper.models import Ad
import re
from bs4 import BeautifulSoup

def index(request):
    listings_url = 'http://newyork.craigslist.org/search/mis?query=w4m'
    listings_response = urlib2.urlopen(listings_url)
    listings_html = listings_response.read()

    pool = BeautifulSoup(listings_html)
    ad_rows = pool.findAll('p', attrs={'class' : 'row'})

    for ad_row in ad_rows:
        for link in result.findAll('a'):
            # TODO - global init to compile regex
            p = re.compile(r'(\d+).html')
            ad = link["href"]
            cl_id_match = p.search(ad)
            cl_id = cl_id_match.group(1)

             

            

    
