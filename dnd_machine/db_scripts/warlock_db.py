from character_builder.models import Class, Skill, Proficiency, SavingThrow
from character_builder.serializers import ClassSerializer, ProficiencySerializer, SavingThrowSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class_ = Class.objects.create(class_name='Warlock',
                              hit_die=8,
                              from_skills_choose=2)

Skill.objects.create(class_name=class_,
                     skill='Arcana')

Skill.objects.create(class_name=class_,
                     skill='Deception')

Skill.objects.create(class_name=class_,
                     skill='History')

Skill.objects.create(class_name=class_,
                     skill='Intimidation')

Skill.objects.create(class_name=class_,
                     skill='Investigation')

Skill.objects.create(class_name=class_,
                     skill='Nature')

Skill.objects.create(class_name=class_,
                     skill='Religion')

Proficiency.objects.create(class_name=class_,
                           proficiency='Light Armor',
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

warlock_class_serializer = ClassSerializer(instance=class_)
warlock_class_serializer.data