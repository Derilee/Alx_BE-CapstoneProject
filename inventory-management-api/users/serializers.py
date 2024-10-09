from rest_framework import serializers
from .models import User, Profile
from django.contrib.auth import authenticate


#Serializes the fields in the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


# Serializes the fields to display in the Profile model
class ProfileSerializer(serializers.ModelSerializer):
    # A user field using the UserSerializer, set to read-only to prevent modifications through the API.
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'staff_id', 'position', 'profile_picture']

    # validate staff_id to make sure each staff has a unique id
    def validate(self, data):
        if Profile.objects.filter(staff_id=data).exists():
            raise serializers.ValidationError('Staff ID already exists')
        return data
 

#creates a register serializer to serialize the fields needed for user registration
class RegisterSerializer(serializers.ModelSerializer):
    # A custom password field is created and set to write-only to ensure it isn't exposed in API responses.
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    #this method creates a user with the data provided
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    #validates the user credentials if valid to login
    def validate(self, data):
        username = data.get('username') #get the username data the user inputs
        password = data.get('password') #get the password data the user inputs
        user = authenticate(username=data['username'], password=data['password']) #authenticate if the gotten data matches user data in the DB
        if user and user.is_active:
            return user
        raise serializers.ValidationError('invalid credentials')
