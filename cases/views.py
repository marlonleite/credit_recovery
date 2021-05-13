from rest_framework import viewsets

from cases.models import CaseModel
from cases.serializers import CaseSerializer


class CaseViewSet(viewsets.ModelViewSet):
    queryset = CaseModel.objects.all()
    serializer_class = CaseSerializer
    http_method_names = ("get", "post", "patch", "delete")
