from rest_framework import serializers
from .models import VeiwerForm,ParticipateForm

class VeiwerFormSerializers(serializers.ModelSerializer):
    class Meta:
        model=VeiwerForm
        fields='__all__'

class ParticipateFormSerializers(serializers.ModelSerializer):
    class Meta:
        model=ParticipateForm
        fields='__all__'





