from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import random, string, json
from django.db.models import F
import re
from django.http import QueryDict
from Crypto.PublicKey import RSA
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
        return Response(item.data)
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
        # c_u = Accounts.objects.values('username').get(email__iexact=item['email'])['username']
        if c_username == Accounts.objects.values('username').get(email__iexact=item['email'])['username']:
            if c_password == Accounts.objects.values('password').get(username__iexact=item['username'])['password']:
                data = {"c_email":c_email, 'c_username': c_username}
                k = Accounts.objects.values('key_pair').get(username__iexact=item['username'])['key_pair'] 
                k=k.split('|')
                data['public_key'] = k[1]
                data['private_key'] = k[0]
            
            else: data['Error'] = ("INCORRECT PASSWORD")
        else: data['Error'] = ("INCORRECT USERNAME OR PASSWORD")
    else: data['Error'] = ("USER DOES NOT EXSIST PLEASE SIGN UP") 

    return Response(data)


@api_view(['POST'])
def transaction_view(request):
    pass