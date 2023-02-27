from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    score = models.IntegerField(default=0)
    time= models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.user.username


class Ques(models.Model):
    id=models.IntegerField(primary_key=True)
    ans = models.CharField(max_length=200,null=True)
    direction=models.CharField(max_length=200,null=True)
    def __int__(self):
        return self.id        