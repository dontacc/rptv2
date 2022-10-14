from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True,null=True,blank=True)
    phone = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

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
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.type
