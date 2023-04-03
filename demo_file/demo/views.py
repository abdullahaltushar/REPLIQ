from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceLogList(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated]
