from rest_framework.views import APIView
import random
from django.urls import reverse
from rest_framework.generics import UpdateAPIView
from .Serializers import PasswordSerializer, VerifySerializer
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from core.models import User, password_reset_token_created


class ForgotPassword(APIView):
    serializer_class = PasswordSerializer

    def post(self, arg):
        d = self.request.data
        phone = d["phone"]
        queryset = User.objects.filter(phone=phone).values_list('uid')

        token = password_reset_token_created(
            user_id=queryset,
            number=random.randint(1000, 9999),
        )

        is_token_exist = password_reset_token_created.objects.filter(user__phone=phone)
        if queryset.exists():

            if is_token_exist.exists():
                is_token_exist.delete()
                token.save()
                print(token.number)
            else:
                print(token.number)
                token.save()
            for x in queryset:
                for a in x:
                    return HttpResponseRedirect(
                        redirect_to='http://localhost:8000{}'.format(reverse('verify', kwargs={'user_id': str(a)})))

        else:
            return Response('phone is not exist', status=status.HTTP_404_NOT_FOUND)


class VerifyCode(UpdateAPIView):
    serializer_class = VerifySerializer
    lookup_field = 'user_id'

    def get_queryset(self):
        pass

    def put(self, request, *args, **kwargs):
        user = self.kwargs.get('user_id')
        queryset = password_reset_token_created.objects.filter(user_id=user)
        dbcode = queryset.values_list('number', flat=True)
        print(dbcode)
        yourcode = self.request.data['code']
        for sentcode in dbcode:
            if sentcode == yourcode:
                return HttpResponseRedirect(
                    redirect_to='http://localhost:8000{}'.format(reverse('password_reset_confirm')))
            else:
                return HttpResponseRedirect(
                    redirect_to='http://localhost:8000{}'.format(reverse('rest_password_reset')))
        return self.retrieve(request, *args, **kwargs)
