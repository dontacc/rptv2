from rest_framework import serializers
from .models import Order
from core.models import User

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['type','payment_status','customer']



