from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import *
import ast
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def languages(request):
    langs = Language.objects.all()
    llangs = [lang.name + " " + str(lang.language_id) + "<br />" for lang in langs]
    return HttpResponse(llangs)

def film(request, id):
    try:
        film = Film.objects.get(film_id=id)
        data = serializers.serialize('python', [film])
        return JsonResponse(data, safe=False)
    except Film.DoesNotExist as e:
        return HttpResponse("Film not found", status=404)

@csrf_exempt 
def film_action(request):
    if request.method == 'PUT' and len(request.body) > 0:
        body = json.loads(str(request.body, 'utf-8'))
        try:
            id = body['id']
            # TODO inne pola - dynamicznie najlepiej 
            Film.objects.filter(film_id=id).update(title=body['title'])
            film = Film.objects.get(film_id=id)
            return HttpResponse(film)
        except KeyError as e:
            print("Parameter {} not found".format(e))        
            return HttpResponse("Parameter {} not found".format(e))
    return HttpResponse("costam")  