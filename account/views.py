from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet,ReadOnlyModelViewSet
from .Serializers import OrderSerializers, CustomerSerializers
from .models import Customer, Order
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from account.sms import send_otp_to_phone
from core.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('username')
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    permission_classes = [permissions.DjangoModelPermissions]

    @action(detail=False,methods=['GET','PUT'],permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        (customer,created) = Customer.objects.get_or_create(user_id=request.user.id)
        if request.method=='GET':
            serializer = CustomerSerializers(customer)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer = CustomerSerializers(customer,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class OrderViewSet(ModelViewSet):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [permissions.DjangoModelPermissions ]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        (customer_id,created)=Customer.objects.only('id').get_or_create(user_id=self.request.user.id)
        return Order.objects.filter(customer_id=customer_id)
