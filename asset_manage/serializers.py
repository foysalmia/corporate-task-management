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

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','user','name','company','designation']

class GetEmployeeSerializer(serializers.ModelSerializer):
    company = SimpleCompanySerializer(read_only = True)
    class Meta:
        model = Employee
        fields = ['id','user','name','company','designation']

class DeviceLogSerializer(serializers.ModelSerializer):
    '''This serializer is for Device Log's POST,PUT,PATCH,DELETE methods'''
    class Meta:
        model = DeviceLog
        fields = ['device','employee','checkout_time','return_time','checkout_condition','return_condition']

class GetDeviceLogSerializer(serializers.ModelSerializer):
    '''This serializer is for Device Log's GET methods'''
    device = GetDeviceSerializer(read_only = True)
    employee = GetEmployeeSerializer(read_only = True)
    class Meta:
        model = DeviceLog
        fields = ['device','employee','checkout_time','return_time','checkout_condition','return_condition']


