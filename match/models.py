from django.db import models
from django.core.validators import RegexValidator
from phone_field import PhoneField

class VeiwerForm(models.Model):
    WOMAN = 'W'
    MAN = 'M'
    GENRE_CHOICES = [
        (WOMAN, 'Woman'),
        (MAN, 'Man'),
    ]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender=models.CharField(max_length=1, choices=GENRE_CHOICES, default='-')
    city=models.CharField(max_length=200)
    birth_date=models.DateField()
    id_card=models.CharField(max_length=10,validators=[RegexValidator(r'^\d{10}$')])
    phone = PhoneField(unique=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class ParticipateForm(models.Model):
    WOMAN = 'W'
    MAN = 'M'
    GENRE_CHOICES = [
        (WOMAN, 'Woman'),
        (MAN, 'Man'),
    ]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    id_card=models.CharField(max_length=10,validators=[RegexValidator(r'^\d{10}$')])
    birth_date=models.DateField()
    gender=models.CharField(max_length=1, choices=GENRE_CHOICES, default='-')
    degree= models.CharField(max_length=200)
    major=models.CharField(max_length=200)
    job=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = PhoneField(unique=True)
    phone2 = PhoneField(unique=True)
    image=models.ImageField(upload_to='match/profile')
    def __str__(self):
        return f'{self.first_name} {self.last_name}'