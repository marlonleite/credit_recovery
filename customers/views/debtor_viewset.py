from rest_framework import viewsets

from customers.models import DebtorModel
from customers.serializers import DebtorSerializer


class DebtorViewSet(viewsets.ModelViewSet):
    queryset = DebtorModel.objects.all()
    serializer_class = DebtorSerializer
    http_method_names = ("get", "post", "patch", "delete")
