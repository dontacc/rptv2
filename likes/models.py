from django.db import models
from django.conf import settings

class Likes(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
