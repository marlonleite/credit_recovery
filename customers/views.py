from rest_framework import viewsets

from customers.models import CreditorModel, DebtorModel
from customers.serializers import CreditorSerializer, DebtorSerializer


class CreditorViewSet(viewsets.ModelViewSet):
    queryset = CreditorModel.objects.all()
    serializer_class = CreditorSerializer
    http_method_names = ("get", "post", "patch", "delete")


class DebtorViewSet(viewsets.ModelViewSet):
    queryset = DebtorModel.objects.all()
    serializer_class = DebtorSerializer
    http_method_names = ("get", "post", "patch", "delete")
