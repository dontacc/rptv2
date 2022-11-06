from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import uuid


class User(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_card = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    is_active = models.BooleanField(default=True)
    phone_regex = RegexValidator(regex=r'^(\+98?)?{?(0?9[0-9]{9,9}}?)$')
    phone = models.CharField(validators=[phone_regex], max_length=11, unique=True, null=True, blank=True)
    # phone_regex=RegexValidator(regex=r'^(\+98?)?{?(0?9[0-9]{9,9}}?)$')
    REQUIRED_FIELDS = [ 'email', 'id_card','phone']

