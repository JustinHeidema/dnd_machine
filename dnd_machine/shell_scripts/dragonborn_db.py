from character_builder.models import Race, RaceTrait, Language
from character_builder.serializers import RaceSerializer, RaceTraitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

dragonborn = Race.objects.create(race_name='Dragonborn',
                                 strength_modifier=2,
                                 charisma_modifier=1,
                                 speed=30)

RaceTrait.objects.create(race_name=dragonborn,
                         trait_name='Draconic Ancestry',
                         trait_effect='You have draconic ancestry.'
                                      'Choose one type of dragon from the D raconic Ancestry'
                                      'table. Your breath weapon and damage resistance are'
                                      'determined by the dragon type, as show n in the table.')
RaceTrait.objects.create(race_name=dragonborn,
                         trait_name='Breath Weapon',
                         trait_effect='You can use your action to exhale'
                                      'destructive energy. Your draconic ancestry determines'
                                      'the size, shape, and damage type of the exhalation.'
                                      'W hen you use your breath weapon, each creature in'
                                      'the area of the exhalation must make a saving throw,'
                                      'the type of which is determined by your draconic'
                                      'ancestry. The DC for this saving throw equals 8 +'
                                      'your Constitution m odifier + your proficiency bonus. A'
                                      'creature takes 2d6 damage on a failed save, and half'
                                      'as much damage on a successful one. The damage'
                                      'increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6'
                                      'at 16th level.'
                                      'After you use your breath weapon, you can’t use it'
                                      'again until you com plete a short or long rest')

RaceTrait.objects.create(race_name=dragonborn,
                         trait_name='Damage Resistance',
                         trait_effect='You have resistance to the damage type'
                                      ' associated with your draconic ancestry')

Language.objects.create(race_name=dragonborn,
                        language='Common')

Language.objects.create(race_name=dragonborn,
                        language='Draconic')

dragonborn_serializer = RaceSerializer(instance=dragonborn)
dragonborn_serializer.data
