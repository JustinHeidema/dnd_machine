from character_builder.models import Race, RaceTrait, Language
from character_builder.serializers import RaceSerializer, RaceTraitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

race = Race.objects.create(race_name='Elf',
                           dexterity_modifier=2,
                           speed=25)

RaceTrait.objects.create(race_name=race,
                         trait_name='Darkvision',
                         trait_effect='Accustomed to twilit forests and the night'
                                      'sky, you have superior vision in dark and dim conditions.'
                                      'You can see in dim light within 60 feet of you as if it'
                                      'were bright light, and in darkness as if it were dim light.'
                                      'You can\'t discern color in darkness, only shades of gray.')

RaceTrait.objects.create(race_name=race,
                         trait_name='Keen Senses',
                         trait_effect='You have proficiency in the Perception skill')

RaceTrait.objects.create(race_name=race,
                         trait_name='Fey Ancestry',
                         trait_effect='You have advantage on saving throws'
                                      'against being charmed, and magic can\'t put you to sleep')

RaceTrait.objects.create(race_name=race,
                         trait_name='Trance',
                         trait_effect='Elves don\'t need to sleep. Instead, they'
                                      ' meditate deeply, remaining semiconscious, for 4'
                                      '  a day. (The Common word for such meditation'
                                      ' is \"trance.\") While meditating, you can dream after a'
                                      ' fashion; such dream s are actually mental exercises that'
                                      ' have become reflexive through years of practice. After'
                                      ' resting in this way, you gain the sam e benefit that a'
                                      ' human does from 8 hours of sleep')

Language.objects.create(race_name=race,
                        language='Common')

Language.objects.create(race_name=race,
                        language='Elvish')

race_serializer = RaceSerializer(instance=race)
race_serializer.data
