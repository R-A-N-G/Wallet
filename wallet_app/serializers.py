from django.db.models import fields
from rest_framework import serializers
from .models import Accounts
  
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('email', 'username', 'password',)