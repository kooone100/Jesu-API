from rest_framework import permissions, generics, viewsets
from .models import Measurement, Customers
from .serializers import (UserSerializer, MeasurementSerializer, CustomersSerializer)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

