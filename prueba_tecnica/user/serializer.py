from rest_framework import serializers
from user.models import UserModel
from django.core.exceptions import ValidationError

# Serializer converts the data JSON from tha front to the back-end mapped to the ORM model 
class UserSignupSerializer(serializers.ModelSerializer):
    class Meta: # Dado que hay modelos para serializar, se debe agregar la clase Meta:
        model = UserModel # Utilizar explícitamente el modelo de usuario
        fields = '__all__' # Use los campos para aclarar campos, el nombre de la tabla __all__ contiene todos los campos
        extra_kwargs = {
            'password':{'write_only': True}, # para no mostrar la contraseña en la respuesta del servicio
        }
    
    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        user.save()
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    # this is needed for the login
    email = serializers.EmailField(max_length = 50)
    password = serializers.CharField(max_length = 100)

    class  Meta:
        model = UserModel
        fields = '__all__'