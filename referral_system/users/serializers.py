from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'invite_code', 'activated_invite_code', 'referred_by']

    def validate_phone_number(self, value):
        # Проверка, что номер телефона не существует в базе данных
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Пользователь с таким номером уже существует.")
        return value

class InviteCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['invite_code']

    def validate_invite_code(self, value):
        # Проверка, что инвайт-код существует и не был уже использован
        if not User.objects.filter(invite_code=value).exists():
            raise serializers.ValidationError("Этот инвайт-код не существует.")
        return value