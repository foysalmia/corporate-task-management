from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('company',CompanyViewSet,basename='company')
router.register('device',DeviceViewSet,basename='device')

urlpatterns = router.urls
