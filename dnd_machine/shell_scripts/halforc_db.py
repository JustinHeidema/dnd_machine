from character_builder.models import Race, RaceTrait, Language
from character_builder.serializers import RaceSerializer, RaceTraitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

halforc = Race.objects.create(race_name='Halforc',
                              strength_modifier=2,
                              constitution_modifier=1,
                              speed=30)

RaceTrait.objects.create(race_name=halforc,
                         trait_name='Darkvision',
                         trait_effect='Thanks to your orc blood, you have'
                                      'superior vision in dark and dim conditions. You can'
                                      'see in dim light within 60 feet of you as if it w ere bright'
                                      'light, and in darkness as if it w ere dim light. You can\'t'
                                      'discern color in darkness, only shades o f gray')

RaceTrait.objects.create(race_name=halforc,
                         trait_name='Menacing',
                         trait_effect='You gain proficiency in the'
                                      'Intimidation skill.')

RaceTrait.objects.create(race_name=halforc,
                         trait_name='Relentless Endurance',
                         trait_effect='W hen you are reduced to'
                                      '0 hit points but not killed outright, you can drop to 1 hit'
                                      'point instead. You can’t use this feature again until you'
                                      'finish a long rest.')

RaceTrait.objects.create(race_name=halforc,
                         trait_name='Savage Attacks',
                         trait_effect='W hen you score a critical hit with'
                                      'a melee weapon attack, you can roll one of the w eapon\'s'
                                      'damage dice one additional time and add it to the extra'
                                      'damage of the critical hit.')

Language.objects.create(race_name=halforc,
                        language='Common')

Language.objects.create(race_name=halforc,
                        language='Orc')

halforc_serializer = RaceSerializer(instance=halforc)
halforc_serializer.data
