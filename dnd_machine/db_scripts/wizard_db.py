from character_builder.models import Class, Skill, Proficiency, SavingThrow
from character_builder.serializers import ClassSerializer, ProficiencySerializer, SavingThrowSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class_ = Class.objects.create(class_name='Wizard',
                              hit_die=6,
                              from_skills_choose=2)

Skill.objects.create(class_name=class_,
                     skill='Arcana')
Skill.objects.create(class_name=class_,
                     skill='History')
Skill.objects.create(class_name=class_,
                     skill='Insight')
Skill.objects.create(class_name=class_,
                     skill='Investigation')
Skill.objects.create(class_name=class_,
                     skill='Medicine')
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
                           short_name='INT',
                           long_name='Intelligence')

SavingThrow.objects.create(class_name=class_,
                           short_name='WIS',
                           long_name='Wisdom')

wizard_class_serializer = ClassSerializer(instance=class_)
wizard_class_serializer.data