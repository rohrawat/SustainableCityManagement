from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import requests
import json


@api_view()
def PollutionView(request):
    response = requests.get('http://erc.epa.ie/real-time-air/www/aqindex/aqih_json.php')
    return HttpResponse(json.dumps(response.json()),content_type="application/json")

def DublinBikeView(request):
    try:
     response = requests.get(' https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=77cf7ab00377c7f4cc621765273db0e7daf18f82')
    except:
        raise Exception("An exception occurred")
    
    return HttpResponse(json.dumps(response.json()),content_type="application/json")
@api_view()
def EventView(request):
    response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?city=Dublin&apikey=u2MCIW0dPwxqAZMCssL2PrGWWfdkGedj')
    return HttpResponse(json.dumps(response.json()), content_type="application/json")

@api_view()
def dubbike(request):
    response = requests.get('https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=77cf7ab00377c7f4cc621765273db0e7daf18f82')
    response = response.json()
    data = []
    for x in range(len(response)):
        Data = {}
        Data['label'] = response[x]['name']
        Data['value'] = str(response[x]['available_bikes'])
        data.append(Data)
    return HttpResponse(json.dumps(data), content_type="application/json")
