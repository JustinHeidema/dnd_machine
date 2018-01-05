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
        serializer = ClassSerializer(class_)
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
    character = Character.objects.create(name=request.POST['character_name'],
                                         race=request.POST['race_name'],
                                         _class=request.POST['class_name'],
                                         strength=request.POST['strength'],
                                         dexterity=request.POST['dexterity'],
                                         constitution=request.POST['constitution'],
                                         intelligence=request.POST['intelligence'],
                                         wisdom=request.POST['wisdom'],
                                         charisma=request.POST['charisma'])

    component = 'static/src/character.js'



    skill_array = []
    if (character._class == 'Barbarian' or \
                    character._class == 'Cleric' or
                    character._class == 'Druid' or
                    character._class == 'Fighter' or
                    character._class == 'Monk' or
                    character._class == 'Paladin' or
                    character._class == 'Sorcerer' or
                    character._class == 'Warlock' or
                    character._class == 'Wizard'):
        for i in range(2):
            skill = request.POST['skill' + str(i)]
            Skill.objects.create(character=character,
                                 skill=skill)
            skill_array.append(skill)

    elif (character._class == 'Bard'
                              'Ranger'):
        for i in range(3):
            skill = request.POST['skill' + str(i)]
            Skill.objects.create(character=character,
                                 skill=skill)
            skill_array.append(skill)

    elif (character._class == 'Rogue'):
        for i in range(4):
            skill = request.POST['skill' + str(i)]
            Skill.objects.create(character=character,
                                 skill=skill)
            skill_array.append(skill)

    num_languages = request.POST['num_languages']
    language_array = []
    for i in range(int(num_languages)):
        language = request.POST['languages' + str(i)]
        Language.objects.create(character=character,
                                language=language)
        language_array.append(language)

    num_race_traits = request.POST['num_race_traits']
    race_traits = []
    for i in range(int(num_race_traits)):
        trait_name = request.POST['trait_name' + str(i)]
        trait_effect = request.POST['trait_effect' + str(i)]

        RaceTrait.objects.create(character=character,
                                 trait_name=trait_name,
                                 trait_effect=trait_effect)

        dict = {'trait_name': trait_name,
                'trait_effect': trait_effect}

        race_traits.append(dict)

    for i in range(2):
        saving_throw_long_name = request.POST['saving_throw_long_name' + str(i)]
        saving_throw_short_name = request.POST['saving_throw_short_name' + str(i)]
        SavingThrow.objects.create(character=character,
                                   short_name=saving_throw_short_name,
                                   long_name=saving_throw_long_name)

    num_proficiencies = int(request.POST['num_proficiencies'])
    for i in range(num_proficiencies):
        proficiency = request.POST['proficiencies' + str(i)]
        proficiency_type = request.POST['proficiencies_type' + str(i)]
        Proficiency.objects.create(character=character,
                                   proficiency=proficiency,
                                   proficiency_type=proficiency_type)



    props = {
        'id': character.id,
        'name': character.name,
        'race': character.race,
        '_class': character._class,
        'strength': character.strength,
        'dexterity': character.dexterity,
        'constitution': character.constitution,
        'intelligence': character.intelligence,
        'wisdom': character.wisdom,
        'charisma': character.charisma,
        'skill_array': skill_array,
        'language_array': language_array,
        'race_traits': race_traits

    }
    context = {
        'component': component,
        'props': props
    }
    return render(request, 'character_builder/character_review.html', context)


def test(request):
    return render(request, 'character_builder/race_api_template.html')
