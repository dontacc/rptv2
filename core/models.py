import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField

class User(AbstractUser):
    phone = PhoneField(unique=True)
    # phone_regex=RegexValidator(regex=r'^(\+98?)?{?(0?9[0-9]{9,9}}?)$')
    REQUIRED_FIELDS = ['phone']




