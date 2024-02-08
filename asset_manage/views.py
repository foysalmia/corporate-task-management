from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly,IsAuthenticated

from .serializers import *
from .models import *

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdminUser()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetEmployeeSerializer
        return EmployeeSerializer

class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetDeviceSerializer
        return DeviceSerializer

class DeviceLogViewSet(ModelViewSet):
    queryset = DeviceLog.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetDeviceLogSerializer
        return DeviceLogSerializer
