import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
from core.models import User

def send_otp_tp_phone(phone):
    try:
        active_code = random.randint(1000, 9999)
        url = f''
        response = requests.get(url)
    except Exception as e:
        return e


@api_view(['POST'])
def send_otp(request):
    data = request.data
    if data.get('phone') is None:
        return Response({
            'status': 400,
            'message': 'key phone_number is required'
        })
    user=User.objects.create(phone=data.get('phone'),active_code=send_otp_tp_phone(data.get('phone')))
    user.save()
    return Response({
        'status': 200,
        'message': 'otp sent'
    })
    # print('create_otp')
    # active_code = input('active code:')
    # user: User = User.objects.filter(username=instance.username).first()
    # if user.is_active == active_code:
    #     if not user.is_active:
    #         user.is_active = True
    #         user.active_code = random.randint(1000, 9999)
    #         user.save()
    #         print(user.active_code)
    #         return HttpResponse('activated')
    #
    # else:
    #     return HttpResponse('code is not correct')
