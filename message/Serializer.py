from rest_framework import serializers
from . import models
class AddPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Score
        fields = ['phone','user']

class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Score
        fields = ['otp','user']