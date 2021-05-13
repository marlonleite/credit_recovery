import pytest

from customers.serializers import CreditorSerializer


@pytest.mark.django_db
class TestCreditorSerializer:
    @pytest.mark.unit
    def test_serialize_model(self, data):
        serializer = CreditorSerializer(data)
        assert serializer.data

    @pytest.mark.unit
    def test_serialized_data(self, data):
        serializer = CreditorSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.errors == {}
