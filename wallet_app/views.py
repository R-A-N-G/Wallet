import code
from email import message
from turtle import pu
from xml.dom.expatbuilder import TEXT_NODE
from cv2 import estimateChessboardSharpness
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
from Crypto.Cipher import PKCS1_OAEP
import binascii
import codecs
import json
from hashlib import sha512
import time

# API imports here
from .models import *
from .serializers import  *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework import status
 
  
Key = b"-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDSXduJaq2xNGWwGIimwZDHvAkvls2SG4uuB6pTp+70PJc80Hwa\nththYprtYaw4dF1UKHnSVvuo1q+XbEXW727NTMZKH7PPN5Ajz4V6aOcTMjBwDD8H\nOUTHbdyiasQXlNYIqPxhBkmZWPqDhPq7n5voxTBe0xDXtWblU3RnpwUOqQIDAQAB\nAoGAFaIQRv/g78WvJV5IgzmJnXihSzMLXdiWUyW3ptWwtY4bkWXxNT//7dJZk0rF\njqKszFBDQtWuGI1HTl+UiQdjUeqSoYwvR6c3WvaJtaO7Y3DpWRc04yipKbtTDzAY\n2tMoAO9F0rn6MRTTXiLV0DJInZo5ksCnKO+hNlrPHp/bVU8CQQDXDvyIAhRpU7bz\nuCl36/NPXSIiKmi8OQzbR1AlSULVpOAT6P0SpVOaIMAcedGrX8JnBiN0FL7WMRum\nCu9u/uerAkEA+mo1O29p/h2mivt675zIPkNqww1BTzRlVa6oKyeSI8OMn9WvDkDY\nLVT894AFIO50svDbPcoHjwl/dDBERnW++wJBAIEvd3McDLbYmuX8kqx/CEF8aKyt\nXQz0GE0AoZxETemYiSJsqtkwhu/nDIAOjWyssVLB1To93AU+qqUrnHjIltECQQDj\nb4EnmTp4TW/MvTlb1VbdjheyTiCqElmTJ42fnFIT33CiXs6esHBnQ9B57jE6RrmB\nKFbH2O1ikWrMGWZ5ZEnvAkBNZwqX10HQp3QJ2LamMz2JmI+ujCikPOyddAyXIaIr\n0a9CaGO+UyePqcge2VG53rsheoA+kIiPabCukVxp1PHL\n-----END RSA PRIVATE KEY-----"
pubKey = RSA.import_key(Key).public_key()
privateKey = RSA.import_key(Key)





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



list_of_urls = []

@api_view(['POST'])
def login_view(request):
    item = request.data
    global list_of_urls
    c_email = item['email']
    c_username = item['username']
    c_password = item['password']
    
    if "domain" in item:
        domain = item["domain"]
        node = domain
        list_of_urls.append(node)
        list_of_urls = list(set(list_of_urls))

        list_of_url_data = {
            "nodes": list_of_urls
        }
        print(list_of_url_data)
        
        for i in list_of_urls:
            if i != domain:
                requests.post(f"http://{i}/node/register",json = list_of_url_data)

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
                if "domain" in item:
                    data['node_list'] = list_of_urls

   
            else: data['Error'] = ("INCORRECT PASSWORD")
        else: data['Error'] = ("INCORRECT USERNAME OR PASSWORD")
    else: data['Error'] = ("USER DOES NOT EXSIST PLEASE SIGN UP") 

    return Response(data)


# @api_view(['POST'])
# def create_p_2_p_view(request):
#     # domain = request.META['HTTP_HOST']
#     domain = request.data
#     print(domain)
    
    
#     global list_of_urls
#     # node = "http://"+domain+"/transaction/new"

#     # list_of_urls.append(node)
#     # list_of_urls = list(set(list_of_urls))
#     miniers_data = {
#         "nodes" : list_of_urls
#     }

#     return JsonResponse(miniers_data)





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

    msg = json.dumps(tx_data).encode('utf-8')  
    encrypted_data = ""
    encryptor = PKCS1_OAEP.new(pubKey)

    for index in range(0, len(msg), 85):
        encrypted = encryptor.encrypt(msg[index : index + 85])
        encrypted_data += "|" + binascii.hexlify(encrypted).decode()
        
    # print(encrypted_data)


    # decrypt try
    decryptor = PKCS1_OAEP.new(privateKey)
    decryptor_data = encrypted_data.split("|")

    # print(decryptor.decrypt(binascii.unhexlify(decryptor_data[1].encode())))




    encrypted_tx_data = {}
    encrypted_tx_data["enc_tx_data"] = encrypted_data


    #__________________________Publish tx to all node____________________________________________

    # list_of_urls = [("http://127.0.0.1:5000/transaction/new"),("http://127.0.0.1:5001/transaction/new"),("http://127.0.0.1:5002/transaction/new"),("http://127.0.0.1:5003/transaction/new")]
    list_of_urls = [("http://127.0.0.1:5000/transaction/new")]
    # list_of_urls = [("http://192.168.43.108:8000/transaction/new")]   


    def post_url(args):
        return requests.post(args, json = encrypted_tx_data)

    with ThreadPoolExecutor(max_workers=10) as pool:
        response_list = list(pool.map(post_url,list_of_urls))

    for response in response_list:
        res = response.content

    return Response(res)



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
    












