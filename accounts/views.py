from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .Serializers import OrderSerializers,CustomerSerializers
from .models import  Order
from rest_framework.decorators import action
from core.models import User
from rest_framework.response import Response


class CustomerViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerSerializers
    permission_classes = [permissions.DjangoModelPermissions]

    @action(detail=False,methods=['GET','PUT'],permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        (customer,created) = User.objects.get_or_create(user_id=request.user.id)
        if request.method=='GET':
            serializer = CustomerSerializers(customer)
            # print(serializer.data)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer = CustomerSerializers(customer,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)



class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializers
    permission_classes = [permissions.DjangoModelPermissions ]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        (customer_id,created)=User.objects.only('id').get_or_create(user_id=self.request.user.id)
        return Order.objects.filter(customer_id=customer_id)
