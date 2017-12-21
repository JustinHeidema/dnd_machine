from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from character_builder.models import Race, RaceTrait, Language
from character_builder.serializers import  RaceSerializer, RaceTraitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def index(request):
    print("Success")
    return render(request, 'character_builder/index.html')


def race_api(request, pk):
    try:
        race = Race.objects.get(pk=pk.title())
    except Race.DoesNotExist:
        return HttpResponse(status=403)

    if request.method == 'GET':
        serializer = RaceSerializer(race)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RaceSerializer(pk, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        race.delete()
        return HttpResponse(status=204)