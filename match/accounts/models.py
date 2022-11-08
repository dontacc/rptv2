from django.db import models
from django.conf import settings
from movies.models import Movie
from core.models import User

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
    PAYMENT_TYPE_NONE='N'
    PAYMENT_TYPE_ONEMONTHLY = 'O'
    PAYMENT_TYPE_THREEMONTHLY = 'T'
    PAYMENT_TYPE_SIXMONTHLY = 'S'

    PAYMENT_TYPE_CHOICES = [
        (PAYMENT_TYPE_NONE, 'NO ONE'),
        (PAYMENT_TYPE_ONEMONTHLY, 'ONE MONTH'),
        (PAYMENT_TYPE_THREEMONTHLY, 'THREE MONTH'),
        (PAYMENT_TYPE_SIXMONTHLY, 'SIX MONTH'),
    ]

    place_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_TYPE_NONE)
    type = models.CharField(max_length=1, choices=PAYMENT_TYPE_CHOICES, default=None)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.type
    class Meta:
        verbose_name='order'
        verbose_name_plural='orders'

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    user=models.OneToOneField(User,on_delete=models.PROTECT)