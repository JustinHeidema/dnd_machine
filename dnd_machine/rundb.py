import subprocess

character_builder_models = ['from',
                            'character_builder.models',
                            'import',
                            'Race,',
                            'RaceTrait,',
                            'Language']

character_builder_serializer = ['from',
                                'character_builder.serializers',
                                'import',
                                'RaceSerializer,',
                                'RaceTraitSerializer']

rest_framework_renderers = ['from',
                            'character_builder.models',
                            'import',
                            'Race,',
                            'RaceTrait,',
                            'Language']

rest_framework_parsers = ['from',
                          'rest_framework.parsers',
                          'import',
                          'JSONParser']

subprocess.call(['python',
                 'manage.py',
                 'shell'])
subprocess.call(character_builder_models)
subprocess.call(character_builder_serializer)
subprocess.call(rest_framework_renderers)
subprocess.call(rest_framework_parsers)


# from character_builder.models import Race, RaceTrait, Language
# from character_builder.serializers import RaceSerializer, RaceTraitSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
