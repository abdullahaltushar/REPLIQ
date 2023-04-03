from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.company})"


class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    serial_number = models.CharField(max_length=255, unique=True)
    employees = models.ManyToManyField(Employee, through='DeviceLog')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField()
    return_time = models.DateTimeField(null=True, blank=True)
    checkout_condition = models.CharField(
        max_length=255, null=True, blank=True)
    return_condition = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.device} checked out to {self.employee} at {self.checkout_time}"
