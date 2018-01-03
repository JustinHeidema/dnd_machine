from character_builder.models import Class, Skill, Proficiency, SavingThrow
from character_builder.serializers import ClassSerializer, ProficiencySerializer, SavingThrowSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class_ = Class.objects.create(class_name='Paladin',
                              hit_die=10,
                              from_skills_choose=2)

Skill.objects.create(class_name=class_,
                     skill='Athletics')

Skill.objects.create(class_name=class_,
                     skill='Insight')

Skill.objects.create(class_name=class_,
                     skill='Intimidation')

Skill.objects.create(class_name=class_,
                     skill='Medicine')

Skill.objects.create(class_name=class_,
                     skill='Persuasion')

Skill.objects.create(class_name=class_,
                     skill='Religion')


Proficiency.objects.create(class_name=class_,
                           proficiency='All Armor',
                           proficiency_type='Armor')
Proficiency.objects.create(class_name=class_,
                           proficiency='Shields',
                           proficiency_type='Armor')
Proficiency.objects.create(class_name=class_,
                           proficiency='Simple Weapons',
                           proficiency_type='Weapon')
Proficiency.objects.create(class_name=class_,
                           proficiency='Martial Weapons',
                           proficiency_type='Weapon')

SavingThrow.objects.create(class_name=class_,
                           short_name='WIS',
                           long_name='Wisdom')

SavingThrow.objects.create(class_name=class_,
                           short_name='CHA',
                           long_name='Charisma')

paladin_class_serializer = ClassSerializer(instance=class_)
paladin_class_serializer.data
