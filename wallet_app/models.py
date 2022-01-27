from click import password_option
from django.db import models
from Crypto.PublicKey import RSA
from .models import *
def key_pair():
    while True:
        key_pair = RSA.generate(1024)
        print("here")
        private_key = key_pair.exportKey()
        public_key = key_pair.publickey().exportKey()
        # if not Accounts.objects.filter(public_key = public_key).exists():
        keys = f"{public_key}|{private_key}"
        return private_key.decode()

class Accounts(models.Model):
    keys = key_pair
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username 				= models.CharField(max_length=30, unique=True)
    password                = models.CharField(max_length=30)
    key_pair				= models.TextField(max_length=1024, unique=True, default=key_pair)
    # public_key              = models.CharField(max_length=1024, default="fff")
    # private_key             = models.CharField(max_length=1024, default="fff")
    balance					= models.IntegerField(default=100)

    def __str__(self):
        return self.email

