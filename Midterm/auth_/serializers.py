from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        x = [i for i in range(10)]
        print(x)
        if email is None:
            raise serializers.ValidationError('Email must be filled')
        if password is None:
            raise serializers.ValidationError('Password must be filled.')

        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError('Incorrect username')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated')

        return {
            'token': user.token,
        }