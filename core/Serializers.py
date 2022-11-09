from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import DefaultAccountAdapter
from .models import User


class CustomRegisterSerializer(RegisterSerializer):
    phone = serializers.CharField()
    id_card = serializers.CharField(max_length=10)

    def get_cleaned_data(self):
        instance = {
            'phone': self.validated_data.get('phone', ''),
            'id_card': self.validated_data.get('id_card', ''),
            'username': self.validated_data.get('username', ''),
        }
        return instance


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.phone = data.get('phone')
        user.id_card = data.get('id_card')
        user.username = data.get('username')
        user.save()
        return user


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone']


class VerifySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()
