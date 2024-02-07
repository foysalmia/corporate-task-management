from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    company = models.ForeignKey(Company,on_delete = models.CASCADE, related_name = 'employee')
    designation = models.CharField(max_length = 250)

    def name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return str(f"{self.user.first_name} {self.user.last_name}")


class Device(models.Model):
    name = models.CharField(max_length = 250)
    condition = models.CharField(max_length = 250)
    company = models.ForeignKey(Company,on_delete = models.CASCADE, related_name = 'device')

    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device,on_delete = models.CASCADE , related_name = 'log')
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE,  related_name = 'log')
    checkout_time = models.DateField(auto_now_add = True)
    return_time = models.DateField()
    checkout_condition = models.CharField(max_length= 255)
    return_condition = models.CharField(max_length= 255)

    def name(self):
        return self.device.name

