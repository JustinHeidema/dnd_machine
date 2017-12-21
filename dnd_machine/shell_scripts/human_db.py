from character_builder.models import Race, RaceTrait, Language
from character_builder.serializers import RaceSerializer, RaceTraitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

human = Race.objects.create(race_name='Human',
                            strength_modifier=1,
                            dexterity_modifier=1,
                            constitution_modifier=1,
                            wisdom_modifier=1,
                            intelligence_modifier=1,
                            charisma_modifier=1,
                            speed=30)

Language.objects.create(race_name=human,
                        language='Common')

Language.objects.create(race_name=human,
                        language='One extra language of your choice')

human_serializer = RaceSerializer(instance=human)
human_serializer.data
