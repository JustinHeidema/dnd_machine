from character_builder.models import Race, RaceTrait, Language
from character_builder.serializers import  RaceSerializer, RaceTraitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

race = Race.objects.create(race_name='Dwarf',
                           constitution_modifier=2,
                           speed=25)

RaceTrait.objects.create(race_name=race,
                         trait_name='Darkvision',
                         trait_effect='Accustomed to life underground, you'
                                    'have superior vision in dark and dim conditions. You'
                                    'can see in dim light within 60 feet of you as if it were'
                                    'bright light, and in darkness as if it w ere dim light. You'
                                    'can\'t discern color in darkness, only shades of gray.')
RaceTrait.objects.create(race_name=race,
                         trait_name='Dwarven Resilience',
                         trait_effect='You have advantage on saving'
                                       ' throws against poison, and you have resistance'
                                       ' against poison damage')

RaceTrait.objects.create(race_name=race,
                         trait_name='Dwarven Combat Training',
                         trait_effect='You have proficiency'
                                        'with the battleaxe, handaxe, throwing hammer,'
                                        'and warhammer.')

RaceTrait.objects.create(race_name=race,
                         trait_name='Tool Proficiency',
                         trait_effect='You gain proficiency with the'
                                        'artisan\'s tools of your choice: smith\'s tools, brewer\'s'
                                        'supplies, or m ason\'s tools')

RaceTrait.objects.create(race_name=race,
                         trait_name='Stonecunning',
                         trait_effect='Whenever you make an Intelligence'
                                        '(History) check related to the origin of stonework, you'
                                        ' are considered proficient in the History skill and add'
                                        ' double your proficiency bonus to the check, instead of'
                                        ' your normal proficiency bonus')
Language.objects.create(race_name=race,
                        language='Common')

Language.objects.create(race_name=race,
                        language='Dwarvish')

dwarf_race_serializer = RaceSerializer(instance=race)
dwarf_race_serializer.data

