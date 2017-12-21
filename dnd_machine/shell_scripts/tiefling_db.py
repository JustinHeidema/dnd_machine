from character_builder.models import Race, RaceTrait, Language
from character_builder.serializers import RaceSerializer, RaceTraitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

tiefling = Race.objects.create(race_name='Tiefling',
                               intelligence_modifier=2,
                               charisma_modifier=1,
                               speed=25)

RaceTrait.objects.create(race_name=tiefling,
                         trait_name='Darkvision',
                         trait_effect='Thanks to your infernal heritage, you'
                                      'have superior vision in dark and dim conditions. You'
                                      'can see in dim light within 60 feet of you as if it were'
                                      'bright light, and in darkness as if it w ere dim light. You'
                                      'can\'t discern color in darkness, only shades o f gray.')

RaceTrait.objects.create(race_name=tiefling,
                         trait_name='Hellish Resilience',
                         trait_effect='You have resistance to fire damage')

RaceTrait.objects.create(race_name=tiefling,
                         trait_name='Infernal Legacy',
                         trait_effect='You know the thaumaturgy cantrip.'
                                      'Once you reach 3rd level, you can cast the hellish'
                                      'rebuke spell once per day as a 2nd-level spell. O nce you'
                                      'reach 5th level, you can also cast the darkness spell'
                                      'once per day. Charisma is your spellcasting ability for'
                                      'these spells')

Language.objects.create(race_name=tiefling,
                        language='Common')

Language.objects.create(race_name=tiefling,
                        language='Infernal')

tiefling_serializer = RaceSerializer(instance=tiefling)
tiefling_serializer.data
