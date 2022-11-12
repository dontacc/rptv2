from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import uuid

class User(AbstractUser):
    email = models.EmailField(blank=True, null=True,verbose_name='ایمیل')
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_card = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')],unique=True,verbose_name='شماره ملی')
    is_active = models.BooleanField(default=True,verbose_name='فعال بودن ')
    phone_regex = RegexValidator(regex=r'^(\+98?)?{?(0?9[0-9]{9,9}}?)$')
    phone = models.CharField(validators=[phone_regex], max_length=11, unique=True,verbose_name='شماره مبایل')
    REQUIRED_FIELDS = [ 'email', 'id_card','phone']

    class Meta:
        verbose_name='کابر'
        verbose_name_plural='کاربرها'

class password_reset_token_created(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='کاربر')
    number = models.CharField(max_length=4, null=True, blank=True,verbose_name='کد')
    score=models.TimeField(auto_now_add=True,verbose_name='زمان ارسال')

    def __str__(self):
        return self.number
    class Meta:
        verbose_name='کد بازیابی پسورد'
        verbose_name_plural='کدهای بازیابی پسورد'

