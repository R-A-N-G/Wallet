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
        return Response("abcd")


@api_view(['POST'])
def login_view(request):
    item = request.data


@api_view(['POST'])
def transaction_view(request):
    item = request.data