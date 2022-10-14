from rest_framework.viewsets import ModelViewSet,GenericViewSet
from .Serializers import OrderSerializers,CustomerSerializers
from .models import Customer,Order



class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers



