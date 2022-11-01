from rest_framework import serializers
from .models import QandASupport, RefundPolicy, Contact, PrivacyPolicy


class QandASupportSerializers(serializers.ModelSerializer):
    class Meta:
        model = QandASupport
        fields = '__all__'


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class RefundPolicySerializers(serializers.ModelSerializer):
    class Meta:
        model = RefundPolicy
        fields = '__all__'


class PrivacyPolicySerializers(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'
