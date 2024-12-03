from rest_framework import serializers
from .models import User

class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)

class AuthCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    auth_code = serializers.CharField(max_length=4)

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    password = serializers.CharField(write_only=True)

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Пользователь с таким номером уже существует.")
        return value

class InviteCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['invite_code']

    def validate_invite_code(self, value):
        if not User.objects.filter(invite_code=value).exists():
            raise serializers.ValidationError("Этот инвайт-код не существует.")
        return value