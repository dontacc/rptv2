import random
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.core.validators import RegexValidator
from allauth.account.adapter import DefaultAccountAdapter
from .models import User
from django.shortcuts import HttpResponse
from dj_rest_auth.utils import default_create_token, import_callable
from django.conf import settings

class CustomRegisterSerializer(RegisterSerializer):
    phone = serializers.CharField()
    id_card = serializers.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])

    def get_cleaned_data(self):
        print('get_cleaned_data')
        instance={
            'phone': self.validated_data.get('phone', ''),
            'id_card': self.validated_data.get('id_card', ''),
            'username': self.validated_data.get('username', ''),
        }
        return instance



class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        print('save_user')
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.phone = data.get('phone')
        user.id_card = data.get('id_card')
        user.username = data.get('username')
        user.save()
        return user

    # def create_otp(instance):
    #     print('create_otp')
    #     active_code = input('active code:')
    #     user: User = User.objects.filter(username=instance.username).first()
    #     if user.is_active==active_code:
    #         if not user.is_active:
    #             user.is_active = True
    #             user.active_code = random.randint(1000,9999)
    #             user.save()
    #             print(user.active_code)
    #             return HttpResponse('activated')
    #
    #     else:
    #         return HttpResponse('code is not correct')



