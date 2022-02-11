import code
from email import message
from turtle import pu
from xml.dom.expatbuilder import TEXT_NODE
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import random, string, json
from django.db.models import F
import re
from django.http import QueryDict
from Crypto.PublicKey import RSA
from flask import send_from_directory
from rsa import PublicKey
import codecs
import requests
from concurrent.futures import ThreadPoolExecutor
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import codecs
import json
from hashlib import sha512

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
        raise serializers.ValidationError('email id or username already exists')
  
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
                
                # key = k.split(',')
                # pub_key = f"{ key[0] },{ key[1] }"
                # pri_key = f"{ key[2] },{ key[1] }"

                data['public_key'] = k
                data['private_key'] = k

   
            else: data['Error'] = ("INCORRECT PASSWORD")
        else: data['Error'] = ("INCORRECT USERNAME OR PASSWORD")
    else: data['Error'] = ("USER DOES NOT EXSIST PLEASE SIGN UP") 

    return Response(data)


@api_view(['POST'])
def create_p_2_p_view(request):
    pass





@api_view(['POST'])
def transactions_request_view(request):
    values = request.data
    required = ['sender','receiver','amount']
    if not all (k in values for k in required):
        response = {'message' : 'Some Values are Missing'}

    tx_data = {
        "sender":values["sender"],
        "receiver": values["receiver"],
        "amount": values["amount"]
    }

    #__________________________signature_with_sender's_private_key_____________________________

    k = values["sender"].split(",")
    d = int(k[2])
    n = int(k[0])
    msg = json.dumps(tx_data).encode('utf-8')           
    hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
    signature = pow(hash, d, n)

    tx_data["signature"] = signature


    #__________________________encryption_with_receicer's_public_key_____________________________


    #__________________________Publish tx to all node____________________________________________

    list_of_urls = [("http://127.0.0.1:5000/transaction/new"),("http://127.0.0.1:5001/transaction/new"),("http://127.0.0.1:5002/transaction/new"),("http://127.0.0.1:5003/transaction/new")]
    
    def post_url(args):
        return requests.post(args, json=tx_data)

    with ThreadPoolExecutor(max_workers=10) as pool:
        response_list = list(pool.map(post_url,list_of_urls))

    for response in response_list:
        print(response.content)

    return Response(tx_data)

@api_view(['POST'])
def check_balance_view(request):
    values = request.data
    balance = values["balance"]
    sender = values["sender"]

    k = Accounts.objects.values('balance').get(key_pair=sender)['balance']
    res = "True" if int(balance)<k else "False"

    return JsonResponse({"message":res})

@api_view(['POST'])
def transaction_update_view(request):
    item = request.data

    for i in item.values():
        i = i.split("|")
        S = i[0]
        R = i[1]
        A = int(i[2])
        Accounts.objects.filter(key_pair = S).update(balance = F('balance') - A)
        Accounts.objects.filter(key_pair = R).update(balance = F('balance') + A)


    return JsonResponse({"message":"under construction"})
    












