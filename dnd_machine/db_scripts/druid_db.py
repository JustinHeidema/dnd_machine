from character_builder.models import Class, Skill, Proficiency, SavingThrow
from character_builder.serializers import ClassSerializer, ProficiencySerializer, SavingThrowSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class_ = Class.objects.create(class_name='Druid',
                              hit_die=8,
                              from_skills_choose=2)

Skill.objects.create(class_name=class_,
                     skill='Animal Handling')

Skill.objects.create(class_name=class_,
                     skill='Arcana')

Skill.objects.create(class_name=class_,
                     skill='Insight')

Skill.objects.create(class_name=class_,
                     skill='Medicine')

Skill.objects.create(class_name=class_,
                     skill='Nature')

Skill.objects.create(class_name=class_,
                     skill='Perception')

Skill.objects.create(class_name=class_,
                     skill='Religion')

Skill.objects.create(class_name=class_,
                     skill='Survival')

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
                           proficiency='Clubs',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Daggers',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Javelins',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Maces',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Quarterstaffs',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Sickles',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Spears',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Darts',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Slings',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Scimitars',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Herbalism Kit',
                           proficiency_type='Other')

SavingThrow.objects.create(class_name=class_,
                           short_name='INT',
                           long_name='Intelligence')

SavingThrow.objects.create(class_name=class_,
                           short_name='WIS',
                           long_name='Wisdom')

druid_class_serializer = ClassSerializer(instance=class_)
druid_class_serializer.data