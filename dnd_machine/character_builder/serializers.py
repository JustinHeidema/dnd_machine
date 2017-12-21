from rest_framework import serializers
from character_builder.models import Race, RaceTrait, Language


class RaceTraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceTrait
        fields = ('trait_name',
                  'trait_effect')


class RaceSerializer(serializers.ModelSerializer):
    race_traits = RaceTraitSerializer(many=True, read_only=True)
    languages = serializers.StringRelatedField(many=True)

    class Meta:
        model = Race
        fields = ('race_name',
                  'strength_modifier',
                  'dexterity_modifier',
                  'constitution_modifier',
                  'intelligence_modifier',
                  'wisdom_modifier',
                  'constitution_modifier',
                  'speed',
                  'languages',
                  'race_traits')




# class RaceSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     race_name = serializers.CharField(max_length=20, default='')
#
#     strength_modifier = serializers.IntegerField(default=0)
#     agility_modifier = serializers.IntegerField(default=0)
#     constitution_modifier = serializers.IntegerField(default=0)
#     intelligence_modifier = serializers.IntegerField(default=0)
#     wisdom_modifier = serializers.IntegerField(default=0)
#     charisma_modifier = serializers.IntegerField(default=0)
#
#     speed = serializers.IntegerField(default=0)
#
#     def create(self, validated_data):
#         """
#         Create and return a new 'Race' instance, given the validated data.
#         :param validated_data:
#         :return:
#         """
#         return Race.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing 'Race' instance, given the validated data.
#         :param instace:
#         :param validated_data:
#         :return:
#         """
#         instance.race_name = validated_data.get('race_name', instance.race_name)
#
#         instance.strength_modifier = validated_data.get('strength_modifier', instance.strength_modifier)
#         instance.agility_modifier = validated_data.get('agility_modifier', instance.agility_modifier)
#         instance.constitution_modifier = validated_data.get('constitution_modifier', instance.constitution_modifier)
#         instance.intelligence_modifier = validated_data.get('intelligence_modifier', instance.intelligence_modifier)
#         instance.wisdom_modifier = validated_data.get('wisdom_modifier', instance.wisdom_modifier)
#         instance.charisma_modifier = validated_data.get('charisma_modifier', instance.charisma_modifier)
#
#         instance.speed = validated_data.get('speed', instance.speed)
#         instance.save()
#         return instance
#
#
#
# class RaceTraitsSerializer(serializers.Serializer):
#     trait_name = serializers.CharField(max_length=50, default='')
#     trait_effect = serializers.CharField(max_length=1000, default='')
#     race = serializers.ForeignKey(Race, null=True)
#
#     def create(self, validated_data):
#         """
#         Create and return a new 'RaceTrait' instance, given the validated data.
#         :param validated_data:
#         :return:
#         """
#         return RaceTrait.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing 'RaceTrait' instance, given the validated data.
#         :param instance:
#         :param validated_data:
#         :return:
#         """
#
#         instance.trait_name = validated_data.get('trait_name', instance.trait_name)
#         instance.trait_effect = validated_data.get('trait_effect', instance.trait_effect)
#         instance.save()
#         return instance
#
#
# class LanguageSerializer(serializers.Serializer):
#     language = serializers.CharField(max_length=20, default='')
#     character = serializers.ForeignKey(Race, null=True)
#
#     def create(self, validated_data):
#         """
#         Create and return a new 'Language' instance, given the validated data.
#         :param validated_data:
#         :return:
#         """
#         return Language.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing 'Language' instance, given the validated data.
#         :param instance:
#         :param validated_data:
#         :return:
#         """
#
#         instance.language = validated_data.get('language', instance.language)
#         instance.save()
#         return instance


