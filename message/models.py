from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

class Score(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    otp = models.CharField(max_length=4,null=True,blank=True)
    phone_regex=RegexValidator(regex=r'^(\+98?)?{?(0?9[0-9]{9,9}}?)$')
    phone = models.CharField(validators=[phone_regex], max_length=11,unique=True)

