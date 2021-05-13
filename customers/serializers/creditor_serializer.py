from customers.models import CreditorModel
from customers.serializers import PersonSerializerMixin


class CreditorSerializer(PersonSerializerMixin):
    class Meta:
        model = CreditorModel
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        instance = self.Meta.model.objects.create(**validated_data)
        return instance
