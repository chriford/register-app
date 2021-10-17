from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Register(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30)
    examnumber = models.CharField(max_length=12)
    province = models.CharField(max_length=100, null=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname

# Create your models here.
