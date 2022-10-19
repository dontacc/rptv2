from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from movies.permission import FullDjangoModelPermissions
from .Serializers import OrderSerializers, CustomerSerializers
from .models import Customer, Order

from rest_framework.decorators import action


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    def get_permissions(self):
        if self.request.method=='GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False,methods=['GET','PUT'],permission_classes=[IsAuthenticated])
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
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
