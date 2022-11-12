from django.db import models
from django.core.validators import RegexValidator

class VeiwerForm(models.Model):
    WOMAN = 'W'
    MAN = 'M'
    GENRE_CHOICES = [
        (WOMAN, 'Woman'),
        (MAN, 'Man'),
    ]
    first_name = models.CharField(max_length=200,verbose_name='نام')
    last_name = models.CharField(max_length=200,verbose_name='نام خانوادگی')
    gender=models.CharField(max_length=1, choices=GENRE_CHOICES, default='-',verbose_name='جنسیت')
    city=models.CharField(max_length=200,verbose_name='استان محل سکونت')
    birth_date=models.DateField(verbose_name='تاریخ تولد')
    id_card=models.CharField(max_length=10,validators=[RegexValidator(r'^\d{10}$')],verbose_name='کد ملی')
    phone = models.CharField(max_length=11, unique=True,verbose_name='شماره مبایل')
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        verbose_name='تماشاگر'
        verbose_name_plural='تماشاگرها'

class ParticipateForm(models.Model):
    WOMAN = 'W'
    MAN = 'M'
    GENRE_CHOICES = [
        (WOMAN, 'Woman'),
        (MAN, 'Man'),
    ]
    first_name = models.CharField(max_length=200,verbose_name='نام')
    last_name = models.CharField(max_length=200,verbose_name='نام خانوادگی')
    id_card=models.CharField(max_length=10,validators=[RegexValidator(r'^\d{10}$')],verbose_name='کد ملی')
    birth_date=models.DateField(verbose_name='تاریخ تولد')
    gender=models.CharField(max_length=1, choices=GENRE_CHOICES, default='-',verbose_name='جنسیت')
    degree= models.CharField(max_length=200,verbose_name='میزان تحصیلات')
    major=models.CharField(max_length=200,verbose_name='رشته تحصیلی')
    job=models.CharField(max_length=200,verbose_name='شغل')
    city=models.CharField(max_length=200,verbose_name='شهر محل سکونت')
    address = models.CharField(max_length=200,verbose_name='آدرس محل سکونت')
    phone = models.CharField( max_length=11, unique=True,verbose_name='شماره همراه')
    phone2 = models.CharField( max_length=11, unique=True, null=True, blank=True,verbose_name='تلفن ثابت')
    image=models.ImageField(upload_to='match/profile',verbose_name='عکس')
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        verbose_name='شرکت کننده'
        verbose_name_plural='شرکت کنندها'