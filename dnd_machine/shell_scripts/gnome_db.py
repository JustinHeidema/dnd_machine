from character_builder.models import Race, RaceTrait, Language
from character_builder.serializers import RaceSerializer, RaceTraitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

gnome = Race.objects.create(race_name='Gnome',
                           intelligence_modifier=2,
                           speed=25)

RaceTrait.objects.create(race_name=gnome,
                         trait_name='Dark Vision',
                         trait_effect='Accustom ed to life underground, you have'
                                      'superior vision in dark and dim conditions. You can'
                                      'see in dim light within 60 feet of you as if it w ere bright'
                                      'light, and in darkness as if it were dim light. You can\'t'
                                      'discern color in darkness, only shades of gray.')

RaceTrait.objects.create(race_name=gnome,
                         trait_name='Gnome Cunning',
                         trait_effect='You have advantage on all Intelligence, Wisdom,'
                                      ' and Charisma saving throws against magic.')

Language.objects.create(race_name=gnome,
                        language='Common')

Language.objects.create(race_name=gnome,
                        language='Gnomish')

gnome_serializer = RaceSerializer(instance=gnome)
gnome_serializer.data
