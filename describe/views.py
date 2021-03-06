from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from describe.models import Description
import exceptions

def index(request):
    return render_to_response('describe/index.html', context_instance=RequestContext(request))

def submit(request): 
    email=""
    gender=""
    height=0
    age=0
    eyes=""
    hair_color=""
    hair_length=""
    race=""
    tone=""

    try:
        email = request.GET["email"]
        email.lower()
    except:
        pass
    try:
        gender = request.GET["gender"]
        gender = gender.lower()
    except:
        pass
    try:
        age = request.GET["age"]
    except:
        pass
    try:
      #  feet = int(request.GET["height"])
      #  inches = int(request.GET["inches"])
      #  height = inches + (feet * 12)
        height = 20
    except exceptions.ValueError:
        pass
    except:
        pass
    try:
        eyes = request.GET["eyes"]
        eyes = eyes.lower()
    except:
        pass
    try:
        hair_color = request.GET["haircolor"]
        hair_color = hair_color.lower()
    except:
        pass
    try:
        hair_length = request.GET["hairlength"]
        hair_length = hair_length.lower()
    except:
        pass
    try:
        race = request.GET["race"]
        race = race.lower()
    except:
        pass
    try:
        tone = request.GET["tone"]
        tone = tone.lower()
    except:
        pass

    description = Description(email=email, height=height, age=age, gender=gender, hair_color=hair_color, race=race, eyes=eyes, tone=tone)
    description.save()
    
    return render_to_response('describe/submitted.html', context_instance=RequestContext(request))
    
