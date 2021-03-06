from dataclasses import field
from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['first_name', 'last_name', 'username', 'email', 'password']