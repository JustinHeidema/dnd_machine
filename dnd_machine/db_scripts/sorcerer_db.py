from character_builder.models import Class, Skill, Proficiency, SavingThrow
from character_builder.serializers import ClassSerializer, ProficiencySerializer, SavingThrowSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class_ = Class.objects.create(class_name='Sorcerer',
                              hit_die=6,
                              from_skills_choose=2)


Skill.objects.create(class_name=class_,
                     skill='Arcana')

Skill.objects.create(class_name=class_,
                     skill='Deception')

Skill.objects.create(class_name=class_,
                     skill='Insight')

Skill.objects.create(class_name=class_,
                     skill='Intimidation')

Skill.objects.create(class_name=class_,
                     skill='Persuasion')

Skill.objects.create(class_name=class_,
                     skill='Religion')


Proficiency.objects.create(class_name=class_,
                           proficiency='Daggers',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Quarterstaffs',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Darts',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Slings',
                           proficiency_type='Weapon')

SavingThrow.objects.create(class_name=class_,
                           short_name='CON',
                           long_name='Constitution')

SavingThrow.objects.create(class_name=class_,
                           short_name='CHA',
                           long_name='Charisma')

sorcerer_class_serializer = ClassSerializer(instance=class_)
sorcerer_class_serializer.data