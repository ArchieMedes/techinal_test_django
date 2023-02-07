from rest_framework import serializers
from activitie.models import ActivityModel
from django.core.exceptions import ValidationError

# El trabajo principal del serializador es convertir los datos JSON 
# pasados ​​del front-end al back-end en un mapeo de modelo ORM
class ActivitySerializer(serializers.ModelSerializer):
    class Meta: # Dado que hay modelos para serializar, se debe agregar la clase Meta:
        model = ActivityModel # Utilizar explícitamente el modelo de usuario
        exclude = (
            'use_it',
            'user_id',
        )
        extra_kwargs = {
            'user_id': {
                'required': False
            },
        }

class ActivityEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityModel
        exclude = (
            'use_it',
            'user_id',
        )
        extra_kwargs = {
            'user_id': {
                'required': False
            },
            'activity': {
                'required': False
            },
            'type': {
                'required': False
            },
            'participants': {
                'required': False
            },
            'price': {
                'required': False
            },
            'link': {
                'required': False
            },
            'key': {
                'required': False
            },
            'accessibility': {
                'required': False
            },
        }