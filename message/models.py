from django.db import models
from core.models import User
import random
from django.utils import timezone

import datetime

class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=4, null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_item = []
        for i in range(4):
            num = random.choice(number_list)
            code_item.append(num)

        code_string = "".join(str(item) for item in code_item)
        self.number = code_string
        print(code_string)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.number


