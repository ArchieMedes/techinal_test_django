from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from user.serializer import UserSignupSerializer, UserLoginSerializer
from user.models import UserModel
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

# Generates tokens manually.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
    }

# Create your views here.
# Registering an user view
class UserSignupView(APIView):
    def post(self, request): # Registrar: POST method
        serializer = UserSignupSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data, status = status.HTTP_201_CREATED)

# 
class UserLoginView(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True) # Validation method
        email = serializer.data["email"]
        password = serializer.data["password"]
        
        # Authentication method. If user exists, returns an user instance.
        user = authenticate(username = email, password = password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        if user is not None:
            tokens = get_tokens_for_user(user) # generate access and refresh tokens for
            data = {
                'code': '00',
                'message_response': 'Successfully logged in.',
                'tokens': tokens
            }

        return Response(data, status=status.HTTP_200_OK)
# read

