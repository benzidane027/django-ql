from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import profile


class UserSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = profile
        fields = ['email']
class currentUserSerializer(BaseUserRegistrationSerializer):
   
    class Meta:
        model = profile
        fields = ["id",'email',"firstName","lastName"]
        
class createUserSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ["id","email","firstName","lastName","password"]

class deleteUserSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ['id']


