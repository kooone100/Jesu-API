from rest_framework import serializers
from .models import Customers, Measurement
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'full_name', 'mobile_no', 'address']

    def __init__(self, *args, **kwargs):
        super(CustomersSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class MeasurementSerializer(serializers.ModelSerializer):
    customer_full_name = serializers.CharField(source='customer.full_name')

    class Meta:
        model = Measurement
        fields = ['id', 'customer_full_name', 'title', 'len', 'waist', 'amount']

    def __init__(self, *args, **kwargs):
        super(MeasurementSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1
