from django.db import models


class Collection(models.Model):
    title=models.CharField(max_length=200)
    explanation=models.CharField(max_length=200)
    def __str__(self):
        return self.title

class ContactUsQuestions(models.Model):
    title = models.CharField(max_length=200)
    explanation = models.TextField(max_length=500)
    stars=models.PositiveSmallIntegerField()
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title
