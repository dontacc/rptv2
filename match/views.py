from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import ParticipateForm,VeiwerForm
from . import Serializers


class VeiwerFormViewSet(ModelViewSet):
    queryset = VeiwerForm.objects.all()
    serializer_class = Serializers.VeiwerFormSerializers


class ParticipateFormViewSet(ModelViewSet):
    queryset = ParticipateForm.objects.all()
    serializer_class = Serializers.ParticipateFormSerializers
