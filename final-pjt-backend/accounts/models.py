from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers')
