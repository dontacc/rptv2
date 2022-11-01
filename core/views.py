from message.models import Score
from .models import User
from message.Serializer import ActivationSerializer,AddPhoneSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView, UpdateAPIView
import random

class AddPhoneView(CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = AddPhoneSerializer

    def post(self, request, *args, **kwargs):
        otp_send = random.randint(1000, 9999)
        user = request.data.get('user')
        get_phone = request.data.get('phone')
        if get_phone:
            phone = str(get_phone)
            phone = Score.objects.filter(phone__iexact=phone)
            if phone.exists():
                return Response({
                    'status': False,
                    'detail': 'Phone number already exists.'
                })
            else:
                new_number=Score(
                    user_id=user,
                    phone=get_phone,
                    otp=otp_send
                )
                new_number.save()
                print(otp_send)

                # key = send_otp(phone)
                # link = f'API-urls'
                # requests.get(link)
                # User.objects.create(
                #     phone=phone,
                #     otp=key,
                #
                # )
                return Response({
                    'status': True,
                    'detail': 'OTP sent successfully.'
                })


# def send_otp(phone):
#     if phone:
#         key = random.randint(1000,9999)
#         print(key)
#         return key
#     else:
#         return False


class ActivationView(UpdateAPIView):
    queryset = Score.objects.all()
    serializer_class = ActivationSerializer

    def put(self, request, *args, **kwargs):
        user=request.data.get('user')
        otp_receive = Score.objects.filter(user_id=user).first()
        opt_send=request.data.get('otp')
        if otp_receive.otp==opt_send:

            chnge:User=User.objects.filter(uid=user).first()
            chnge.is_active=True
            chnge.save()
            empty_otp:Score=Score.objects.filter(user_id=user).first()
            empty_otp.otp=""
            empty_otp.save()
            return Response({
                'status': 200,
                'detail': 'activate successfully.'
            })
        else:
            return Response({
                'status': False,
                'detail': 'wrong code.'
            })
