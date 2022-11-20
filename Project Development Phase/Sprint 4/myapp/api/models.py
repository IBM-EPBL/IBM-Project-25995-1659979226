from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randrange
import datetime


class User(AbstractUser):
    phone_number = models.CharField(max_length=10)
    otp = models.BooleanField(default=False)

class OTP(models.Model):
    #user = models.ForeignKey(User,null=False)
    phone_number = models.CharField(max_length=10)
    expiration_date = models.DateField(auto_now=False, auto_now_add=False)
    expiration_time = models.TimeField(auto_now_add=False, auto_now=False)
    _otp = models.IntegerField()

    def generate_otp():
        return randrange(99999,999999)

    def generate_expdate():
        dt = datetime.datetime.now()
        return dt.date()

    def generate_exptime():
        dt = datetime.datetime.now() + datetime.timedelta(minutes=7)
        return dt.time()

    def __str__(self) -> str:
        return self.phone_number
