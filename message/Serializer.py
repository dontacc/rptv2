from rest_framework import serializers
from message.models import Score
from core.models import User
class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Score
        fields=['phone']



