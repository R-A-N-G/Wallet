from click import password_option
from django.db import models
from Crypto.PublicKey import RSA

def key_pair():
        key_pair = RSA.generate(1024)
        private_key = key_pair.exportKey()
        public_key = key_pair.publickey().exportKey()
        keys = f"{private_key.decode()}|{public_key.decode}"
        return keys

class Accounts(models.Model):
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username 				= models.CharField(max_length=30, unique=True)
    password                = models.CharField(max_length=30)
    key_pair				= models.CharField(max_length=1024, unique=True, default=key_pair())
    balance					= models.IntegerField(default=100)

    def __str__(self):
        return self.email