from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('company',CompanyViewSet,basename='company')
router.register('employee',EmployeeViewSet,basename='employee')
router.register('device',DeviceViewSet,basename='device')
router.register('device-log',DeviceLogViewSet,basename='device-log')

urlpatterns = router.urls
