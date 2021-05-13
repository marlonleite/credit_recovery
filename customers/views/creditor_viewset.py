from rest_framework import viewsets

from customers.models import CreditorModel
from customers.serializers import CreditorSerializer


class CreditorViewSet(viewsets.ModelViewSet):
    queryset = CreditorModel.objects.all()
    serializer_class = CreditorSerializer
    http_method_names = ("get", "post", "patch", "delete")
