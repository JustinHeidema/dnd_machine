from character_builder.models import Race, RaceTrait, Language
from character_builder.serializers import RaceSerializer, RaceTraitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

halfelf = Race.objects.create(race_name='Halfelf',
                              charisma_modifier=2,
                              speed=30)

RaceTrait.objects.create(race_name=halfelf,
                         trait_name='Darkvision',
                         trait_effect='Thanks to your elf blood, you have'
                                      'superior vision in dark and dim conditions. You can'
                                      'see in dim light within 60 feet of you as if it w ere bright'
                                      'light, and in darkness as if it were dim light. You can’t'
                                      'discern color in darkness, only shades of gray.')
RaceTrait.objects.create(race_name=halfelf,
                         trait_name='Fey Ancestry',
                         trait_effect='You have advantage on saving throws'
                                      'against being charmed, and m agic can’t put you to sleep.')

RaceTrait.objects.create(race_name=halfelf,
                         trait_name='Skill Versatility',
                         trait_effect='You gain proficiency in two skills of your choice')

RaceTrait.objects.create(race_name=halfelf,
                         trait_name='Tool Proficiency',
                         trait_effect='You gain proficiency with the'
                                      'artisan\'s tools of your choice: smith\'s tools, brewer\'s'
                                      'supplies, or m ason\'s tools')

RaceTrait.objects.create(race_name=halfelf,
                         trait_name='Stonecunning',
                         trait_effect='Whenever you make an Intelligence'
                                      '(History) check related to the origin of stonework, you'
                                      ' are considered proficient in the History skill and add'
                                      ' double your proficiency bonus to the check, instead of'
                                      ' your normal proficiency bonus')
Language.objects.create(race_name=halfelf,
                        language='Common')

Language.objects.create(race_name=halfelf,
                        language='Elvish')

Language.objects.create(race_name=halfelf,
                        language='One language of your choice')

halfelf_serializer = RaceSerializer(instance=halfelf)
halfelf_serializer.data
