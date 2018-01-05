from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from character_builder.models import Character, Race, RaceTrait, Language, Class, Proficiency, Skill, SavingThrow
from character_builder.serializers import RaceSerializer, RaceTraitSerializer, ClassSerializer, CharacterSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def index(request):
    print("Success")
    return render(request, 'character_builder/index.html')

def home(request):
    return render(request, 'character_builder/home.html')


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


def class_api(request, pk):
    try:
       class_ = Class.objects.get(pk=pk.title())
    except Class.DoesNotExist:
        return HttpResponse(status=403)

    if request.method == 'GET':
        serializer =ClassSerializer(class_)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClassSerializer(pk, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        class_.delete()
        return HttpResponse(status=204)

def character_api(request, pk):
    try:
       character = Character.objects.get(pk=pk)
    except Class.DoesNotExist:
        return HttpResponse(status=403)

    if request.method == 'GET':
        serializer = CharacterSerializer(character)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CharacterSerializer(pk, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        character.delete()
        return HttpResponse(status=204)


def create_character(request):
    character = Character.objects.create(strength=request.POST['strength'],
                                         dexterity=request.POST['dexterity'],
                                         constitution=request.POST['constitution'],
                                         intelligence=request.POST['intelligence'],
                                         wisdom=request.POST['wisdom'],
                                         charisma=request.POST['charisma'])

    component = 'static/src/character.js'

    props = {
        'id': character.id
    }
    context = {
        'component': component,
        'props': props
    }
    return render(request, 'character_builder/character_review.html', context)





def test(request):
    return render(request, 'character_builder/race_api_template.html')