from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class PrivacyPolicy(models.Model):
    explanation = models.TextField(max_length=500)


class RefundPolicy(models.Model):
    explanation = models.TextField(max_length=500)


class QandASupport(models.Model):
    explanation = models.TextField(max_length=500)
