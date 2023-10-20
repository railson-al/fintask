from rest_framework import serializers
from django.contrib.auth import authenticate

from app_users.models import Sector, Sector_Employee, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        return user



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)

        if user and not user.is_active:
            raise serializers.ValidationError("User can't login")

        if not user:
            raise serializers.ValidationError('Incorrect credentials. Please try again.')


        data['user'] = user
        return data
    



class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

    

class SectorEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector_Employee
        fields = '__all__'