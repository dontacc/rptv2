from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import QandASupport, RefundPolicy, Contact, PrivacyPolicy
from . import Serializers


class QandASupportModelViewSet(ModelViewSet):
    queryset = QandASupport.objects.all()
    serializer_class = Serializers.QandASupportSerializers


class RefundPolicyModelViewSet(ReadOnlyModelViewSet):
    queryset = RefundPolicy.objects.all()
    serializer_class = Serializers.RefundPolicySerializers


class ContactModelViewSet(ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = Serializers.ContactSerializers


class PrivacyPolicyViewSet(ReadOnlyModelViewSet):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = Serializers.PrivacyPolicySerializers
