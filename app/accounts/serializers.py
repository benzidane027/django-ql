from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import profile


class UserSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = profile
        fields = ['email','gender']
class currentUserSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = profile
        fields = ["id",'email',"first_name","last_name",""]
        
class createUserSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ["id","email","first_name","last_name","password"]

class deleteUserSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ['id']


