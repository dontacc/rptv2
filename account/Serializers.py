from rest_framework import serializers
from .models import Customer,Order


class CustomerSerializers(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    class Meta:
        model=Customer
        fields=['id','user_id','phone']

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['type','payment_status','customer']



