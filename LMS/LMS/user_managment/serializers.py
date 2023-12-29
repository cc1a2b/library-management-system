from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'password', 'identification_no', 'registration_no', 'page_no','faculty_id', 'gender_id', 'role_id']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserLogoutSerializer(serializers.Serializer):
    pass


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class GendersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genders
        fields = '__all__'


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'


class DepositoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depositories
        fields = '__all__'


class SemestersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semesters
        fields = '__all__'


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'


class LibrariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libraries
        fields = '__all__'
