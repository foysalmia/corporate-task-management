from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name','description']

class DeviceSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only = True)
    class Meta:
        model = Device
        fields = ['name','condition','company']
