from character_builder.models import Class, Skill, Proficiency, SavingThrow
from character_builder.serializers import ClassSerializer, ProficiencySerializer, SavingThrowSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class_ = Class.objects.create(class_name='Monk',
                              hit_die=8,
                              from_skills_choose=2)

Skill.objects.create(class_name=class_,
                     skill='Acrobatics')

Skill.objects.create(class_name=class_,
                     skill='Athletics')

Skill.objects.create(class_name=class_,
                     skill='History')

Skill.objects.create(class_name=class_,
                     skill='Insight')

Skill.objects.create(class_name=class_,
                     skill='Religion')

Skill.objects.create(class_name=class_,
                     skill='Stealth')

Proficiency.objects.create(class_name=class_,
                           proficiency='Simple Weapons',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Shortswords',
                           proficiency_type='Weapon')

SavingThrow.objects.create(class_name=class_,
                           short_name='STR',
                           long_name='Strength')

SavingThrow.objects.create(class_name=class_,
                           short_name='DEX',
                           long_name='Dexterity')

monk_class_serializer = ClassSerializer(instance=class_)
monk_class_serializer.data
