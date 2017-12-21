from character_builder.models import Race, RaceTrait, Language
from character_builder.serializers import RaceSerializer, RaceTraitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

halfling = Race.objects.create(race_name='Halfling',
                               dexterity_modifier=2,
                               speed=25)

RaceTrait.objects.create(race_name=halfling,
                         trait_name='Lucky',
                         trait_effect='When you roll a 1 on an attack roll, ability'
                                      'check, or saving throw, you can reroll the die and must'
                                      'use the new roll.')

RaceTrait.objects.create(race_name=halfling,
                         trait_name='Brave',
                         trait_effect='You have advantage on saving throws against being'
                                      'frightened')

RaceTrait.objects.create(race_name=halfling,
                         trait_name='Halfling Nimbleness',
                         trait_effect='You can move through the'
                                        'space of any creature that is of a size larger than yours')

Language.objects.create(race_name=halfling,
                        language='Common')

Language.objects.create(race_name=halfling,
                        language='Halfling')

halfling_serializer = RaceSerializer(instance=halfling)
halfling_serializer.data
