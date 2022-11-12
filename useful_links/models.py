from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='تماس با ما'
        verbose_name_plural='پیغام ها'


class PrivacyPolicy(models.Model):
    explanation = models.TextField(max_length=500)
    class Meta:
        verbose_name='پرسش و پاسخ و پشتیبانی'
        verbose_name_plural='پرسش و پاسخ و پشتیبانی'


class RefundPolicy(models.Model):
    explanation = models.TextField(max_length=500)
    class Meta:
        verbose_name='سیاست حفظ حریم خصوصی'
        verbose_name_plural='سیاست حفظ حریم خصوصی'


class QandASupport(models.Model):
    explanation = models.TextField(max_length=500)
    class Meta:
        verbose_name='پرسش و پاسخ '
        verbose_name_plural = 'پرسش و پاسخ ها'
