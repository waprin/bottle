# Create your views here.
from django.http import HttpResponse
from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')
    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(output)

def detail(request, poll_id):
    return HttpResponse("you're looking at %s " %  poll_id);

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're showing results for poll %s." % poll_id)
    
