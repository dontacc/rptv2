from rest_framework.serializers import ModelSerializer
from .models import Customer,Order


class CustomerSerializers(ModelSerializer):
    class Meta:
        model=Customer
        fields=['first_name','last_name','email','phone']

class OrderSerializers(ModelSerializer):
    class Meta:
        model=Order
        fields=['type','payment_status','customer']



