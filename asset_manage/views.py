from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

# Create your views here.
class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
