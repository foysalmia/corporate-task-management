from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name','description']

class SimpleCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name']

class DeviceSerializer(serializers.ModelSerializer):
    '''This serializer is for Device's POST,PUT,PATCH,DELETE methods'''
    class Meta:
        model = Device
        fields = ['id','name','condition','company']

class GetDeviceSerializer(serializers.ModelSerializer):
    '''This serializer is for only Device's GET method'''
    company = SimpleCompanySerializer(read_only = True)
    class Meta:
        model = Device
        fields = ['id','name','condition','company']


