from django.db import models


# Create your models here.
class Race(models.Model):
    race_name = models.CharField(max_length=20,
                                 default='',
                                 primary_key=True)

    strength_modifier = models.IntegerField(default=0)
    dexterity_modifier = models.IntegerField(default=0)
    constitution_modifier = models.IntegerField(default=0)
    intelligence_modifier = models.IntegerField(default=0)
    wisdom_modifier = models.IntegerField(default=0)
    charisma_modifier = models.IntegerField(default=0)

    speed = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % self.race_name


class RaceTrait(models.Model):
    trait_name = models.CharField(max_length=50,
                                  default='')
    trait_effect = models.CharField(max_length=1000,
                                    default='')
    race_name = models.ForeignKey(Race,
                                  related_name='race_traits',
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE)

    character = models.ForeignKey(Race,
                                  related_name='character_race_traits',
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.trait_name


class Language(models.Model):
    language = models.CharField(max_length=20,
                                default='')
    race_name = models.ForeignKey(Race,
                                  related_name='languages',
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE)

    character = models.ForeignKey(Race,
                                  related_name='character_languages',
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.language


class Class(models.Model):
    class_name = models.CharField(max_length=20,
                                  default='',
                                  primary_key=True)
    hit_die = models.IntegerField(default=0)
    from_skills_choose = models.IntegerField(default=0)


class Skill(models.Model):
    skill = models.CharField(max_length=20,
                             default='')
    class_name = models.ForeignKey(Class,
                                   related_name='skills',
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)

    character = models.ForeignKey(Class,
                                  related_name='character_skills',
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.skill


class Proficiency(models.Model):
    proficiency = models.CharField(max_length=20,
                                   default='', )
    proficiency_type = models.CharField(max_length=20,
                                        default='', )
    class_name = models.ForeignKey(Class,
                                   related_name='proficiencies',
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)

    character = models.ForeignKey(Class,
                                  related_name='character_proficiencies',
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE)


class SavingThrow(models.Model):
    short_name = models.CharField(max_length=5,
                                  default='', )
    long_name = models.CharField(max_length=20,
                                 default='', )
    class_name = models.ForeignKey(Class,
                                   related_name='saving_throws',
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)

    character_name = models.ForeignKey(Class,
                                       related_name='character_saving_throws',
                                       null=True,
                                       blank=True,
                                       on_delete=models.CASCADE)


class Character(models.Model):
    race = models.CharField(default='',
                            max_length=20)
    _class = models.CharField(default='',
                              max_length=20)

    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    hit_die = models.IntegerField(default=0)
