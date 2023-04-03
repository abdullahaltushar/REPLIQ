from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    company = CompanySerializer()

    class Meta:
        model = Employee
        fields = ['id', 'user', 'company']


class DeviceSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True)
    company = CompanySerializer()

    class Meta:
        model = Device
        fields = ['id', 'name', 'description',
                  'serial_number', 'employees', 'company']


class DeviceLogSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()
    employee = EmployeeSerializer()

    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'employee', 'checkout_time',
                  'return_time', 'checkout_condition', 'return_condition']
