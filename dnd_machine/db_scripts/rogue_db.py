from character_builder.models import Class, Skill, Proficiency, SavingThrow
from character_builder.serializers import ClassSerializer, ProficiencySerializer, SavingThrowSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class_ = Class.objects.create(class_name='Rogue',
                              hit_die=8,
                              from_skills_choose=4)


Skill.objects.create(class_name=class_,
                     skill='Acrobatics')

Skill.objects.create(class_name=class_,
                     skill='Athletics')

Skill.objects.create(class_name=class_,
                     skill='Deception')

Skill.objects.create(class_name=class_,
                     skill='Insight')

Skill.objects.create(class_name=class_,
                     skill='Intimidation')

Skill.objects.create(class_name=class_,
                     skill='Investigation')

Skill.objects.create(class_name=class_,
                     skill='Perception')

Skill.objects.create(class_name=class_,
                     skill='Performance')

Skill.objects.create(class_name=class_,
                     skill='Persuasion')

Skill.objects.create(class_name=class_,
                     skill='Sleight of Hand')

Skill.objects.create(class_name=class_,
                     skill='Stealth')

Proficiency.objects.create(class_name=class_,
                           proficiency='Light Armor',
                           proficiency_type='Armor')
Proficiency.objects.create(class_name=class_,
                           proficiency='Simple Weapons',
                           proficiency_type='Weapon')
Proficiency.objects.create(class_name=class_,
                           proficiency='Longswords',
                           proficiency_type='Weapon')
Proficiency.objects.create(class_name=class_,
                           proficiency='Rapiers',
                           proficiency_type='Weapon')
Proficiency.objects.create(class_name=class_,
                           proficiency='Shortswords',
                           proficiency_type='Weapon')
Proficiency.objects.create(class_name=class_,
                           proficiency='Crossbows, hand',
                           proficiency_type='Weapon')
Proficiency.objects.create(class_name=class_,
                           proficiency='Thieves Tools',
                           proficiency_type='Other')

rogue_class_serializer = ClassSerializer(instance=class_)
rogue_class_serializer.data