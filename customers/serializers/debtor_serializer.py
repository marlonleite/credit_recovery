from customers.models import DebtorModel
from customers.serializers import PersonSerializerMixin


class DebtorSerializer(PersonSerializerMixin):
    class Meta:
        model = DebtorModel
        fields = "__all__"
