from click import password_option
from django.db import models
from Crypto.PublicKey import RSA
from .models import *
def key_pair():
    while True:
        key_pair = RSA.generate(1024)
        key = f"{key_pair.n},{key_pair.e},{key_pair.d}" 
        return key

class Accounts(models.Model):
    keys = key_pair
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username 				= models.CharField(max_length=30, unique=True)
    password                = models.CharField(max_length=30)
    key_pair				= models.CharField(max_length=1024, unique=True, default=key_pair)
    balance					= models.IntegerField(default=100)

    def __str__(self):
        return self.email

