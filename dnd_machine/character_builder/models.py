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


class RaceTrait(models.Model):
    trait_name = models.CharField(max_length=50,
                                  default='')
    trait_effect = models.CharField(max_length=1000,
                                    default='')
    race_name = models.ForeignKey(Race,
                                  related_name='race_traits',
                                  null=True,
                                  on_delete=models.CASCADE)


class Language(models.Model):
    language = models.CharField(max_length=20,
                                default='')
    race_name = models.ForeignKey(Race,
                                  related_name='languages',
                                  null=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.language



