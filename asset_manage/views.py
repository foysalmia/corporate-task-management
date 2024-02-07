from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetDeviceSerializer
        return DeviceSerializer
