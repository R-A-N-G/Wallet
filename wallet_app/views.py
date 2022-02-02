import code
from turtle import pu
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import random, string, json
from django.db.models import F
import re
from django.http import QueryDict
from Crypto.PublicKey import RSA
from rsa import PublicKey
import codecs
# API imports here

from .models import *
from .serializers import  *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework import status

  
@api_view(['POST'])
def registration_view(request):
    item = request.data

    item = RegistrationSerializer(data=request.data)
    # validating for already existing data

    
    if Accounts.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        data = item.data
        del data['password']
        data['message'] = "REGISTRATION DONE"
        data = dict(reversed(list(data.items())))

        return Response(data)
    else:
        return Response("email id or username already exists")


@api_view(['POST'])
def login_view(request):
    item = request.data
    c_email = item['email']
    c_username = item['username']
    c_password = item['password']
    data = {}
    if Accounts.objects.filter(email__iexact=item['email']):
        if c_username == Accounts.objects.values('username').get(email__iexact=item['email'])['username']:
            if c_password == Accounts.objects.values('password').get(username__iexact=item['username'])['password']:
                data = {"email":c_email, 'username': c_username}
                k = Accounts.objects.values('key_pair').get(username__iexact=item['username'])['key_pair'] 
                key = RSA.importKey(k)
                pr_key = key.exportKey()    ;   k_2 = str(pr_key, 'UTF-8')
                pub_key =key.public_key().exportKey()   ;   k_1 = str(pub_key, 'UTF-8')
                data['public_key'] = k_1
                data['private_key'] = k_2
            
            else: data['Error'] = ("INCORRECT PASSWORD")
        else: data['Error'] = ("INCORRECT USERNAME OR PASSWORD")
    else: data['Error'] = ("USER DOES NOT EXSIST PLEASE SIGN UP") 

    return Response(data)


@api_view(['POST'])
def transaction_view(request):
    item = request.data
    keys = Accounts.objects.all().values_list('key_pair')
    pub_k = [((RSA.importKey(i[0].decode())).publickey().export_key()).decode() for i in keys]
    # for i in pub_k:
    #     print(i,type(i))
    for key, value in item.items():
        tx = str(value).split('|')
        a = int(tx[2])
    

        s = pub_k.index(RSA.importKey(tx[0]).public_key().export_key().decode())
        r = pub_k.index(RSA.importKey(tx[1]).public_key().export_key().decode())

        Accounts.objects.filter(id = s+1).update(balance=F('balance') - a)
        Accounts.objects.filter(id = r+1).update(balance=F('balance') + a)
        
        print(s,r,a)
    
    return Response("done")

    '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8n4ag9vVY92Lex9r4EP57fyTk
Yq40tqBk9+H2vxygVBsPOeq64MOtkEU2z7+/QezpWa51LDlKoBKTm8xkx4e+YYFW
mLzP59Xt/NbUA6JkXUIkhoSmX4R7ViF8o9PPU7csVLBWB7KAtez15Ai66qIZebux
WCGFZOzxcDuZ0GY8vwIDAQAB
-----END PUBLIC KEY-----
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCZs5GG7R6iH795C/5XuDNB6wQF
0A9IpxUwT7a5rMAIXdDwkP6q9RUamVfy0sxoBNrcCsrfNpSjVGvs1WM8afTRQzT2
DCUlNAwAWhgH0kSBjL9oCwTjhBvbm+2ni3gRa80JHfnzwHLJEFgm+vWRtA6PKwsu
jNB91O+hslQp2/nC9wIDAQAB
-----END PUBLIC KEY-----
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCeTMaDqzYu7m2f56a3ZXlyBv70
md/cxBhyddQeqL0Gxd8oxtSsJEHWaFSNAcXJBkt3viCbW9FbxqnjUQ5ZjPZjF3f8
1eS/WNIFn9G1HFrwmUdK+dP6/VQxeZfUVfO1XCCsoPZZD2Wa0ryT9mZehKYaTLBX
CT04aJt3jQwg3XdsiQIDAQAB
-----END PUBLIC KEY-----
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9oqYOizFEDOnhhquutLMP7cuM
U70b0tBXlUwbdc9Mz39wA6fP0M30fYUEPRwicnPwZXbO74iRGMb6fR9AXlS8Hg69
Tj4pl4BGK0c3P8l0ENuFxiy6QgGLvxwmMdS/gqv+9qeaW2FM8wL4YbKi4nLOqzRL
jog+oiQDhQFu6v+DSQIDAQAB
-----END PUBLIC KEY-----'''