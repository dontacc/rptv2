import requests
from django.utils.crypto import get_random_string
from django.conf import settings
def send_otp_to_phone(phone):
    try:
        otp=get_random_string(4),
        url=f'https://2factor.in/API/V1/{settings.api_key}/SMS/{phone}/{otp}'
        response=requests.get(url)
        return otp
    except Exception as e:
        return None