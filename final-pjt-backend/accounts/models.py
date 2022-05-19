from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    score = models.IntegerField(null=True)
    correct = models.IntegerField(null=True)
    wrong = models.IntegerField(null=True)
