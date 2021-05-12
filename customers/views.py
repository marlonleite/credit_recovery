from rest_framework import viewsets

from customers.models import Creditor, Debtor
from customers.serializers import CreditorSerializer, DebtorSerializer


class CreditorViewSet(viewsets.ModelViewSet):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer
    http_method_names = ("get", "post", "patch", "delete")


class DebtorViewSet(viewsets.ModelViewSet):
    queryset = Debtor.objects.all()
    serializer_class = DebtorSerializer
    http_method_names = ("get", "post", "patch", "delete")
