

def baseurl(request):
    print "CONTEXT"
    return {'BASE_URL': 'http://' + request.get_host(),}
