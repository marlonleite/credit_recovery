import pytest

from customers.serializers import DebtorSerializer


@pytest.mark.django_db
class TestDebtorSerializer:
    @pytest.mark.unit
    def test_serialize_model(self, data):
        serializer = DebtorSerializer(data)
        assert serializer.data

    @pytest.mark.unit
    def test_serialized_data(self, data):
        serializer = DebtorSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.errors == {}
