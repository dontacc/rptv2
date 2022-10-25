from djoser.serializers import UserSerializer as BaseUserSerializer ,UserCreateSerializer as BaseUserCreateSerializer
from phone_field import PhoneField
from core.models import User
from rest_framework import serializers

from account.models import Customer,Order
class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        pass
        # fields = ['id', 'username', 'password','re_password', 'email','phone']

class CustomerSerializers(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    class Meta:
        model=Customer
        fields=['id','user_id','phone']
class UserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username',]


