from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token 
from rest_framework.validators import UniqueValidator 

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    
    def validate(self, data):
        if data['password'] != data[password2]:
            raise serializers.ValidationError(
                {"password": "password fields didn't match."}
            )
        return data


    def create(self, validated_date):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['username'])
        user.save()
        token = Token.objects.create(user=user)
        return user