from character_builder.models import Class, Skill, Proficiency, SavingThrow
from character_builder.serializers import ClassSerializer, ProficiencySerializer, SavingThrowSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class_ = Class.objects.create(class_name='Cleric',
                              hit_die=8,
                              from_skills_choose=2)

Skill.objects.create(class_name=class_,
                     skill='History')

Skill.objects.create(class_name=class_,
                     skill='Athletics')

Skill.objects.create(class_name=class_,
                     skill='Intimidation')

Skill.objects.create(class_name=class_,
                     skill='Nature')

Skill.objects.create(class_name=class_,
                     skill='Perception')

Proficiency.objects.create(class_name=class_,
                           proficiency='Light Armor',
                           proficiency_type='Armor')

Proficiency.objects.create(class_name=class_,
                           proficiency='Medium Armor',
                           proficiency_type='Armor')

Proficiency.objects.create(class_name=class_,
                           proficiency='Shields',
                           proficiency_type='Armor')

Proficiency.objects.create(class_name=class_,
                           proficiency='Simple Weapons',
                           proficiency_type='Weapon')

SavingThrow.objects.create(class_name=class_,
                           short_name='WIS',
                           long_name='Wisdom')

SavingThrow.objects.create(class_name=class_,
                           short_name='CHA',
                           long_name='Charisma')

cleric_class_serializer = ClassSerializer(instance=class_)
cleric_class_serializer.data