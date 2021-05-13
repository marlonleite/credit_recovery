import validate_docbr as docbr
from rest_framework import serializers

from customers.models import CreditorModel, DebtorModel


class PersonSerializerMixin(serializers.ModelSerializer):
    def validate_document(self, value):
        if self.Meta.model.objects.filter(document=value).exists():
            raise serializers.ValidationError(f"This document '{value}' is in use.")
        elif len(value) not in [11, 14]:
            raise serializers.ValidationError(
                f"This document '{value}' is invalid size."
            )
        elif not value.isnumeric():
            raise serializers.ValidationError(
                f"This document '{value}' is invalid numeric."
            )
        else:
            docs = (docbr.CPF, value), (docbr.CNPJ, value)
            valid = docbr.validate_docs(docs)
            if not any(valid):
                raise serializers.ValidationError(
                    f"This document '{value}' is invalid."
                )
        return value

    def validate_email(self, value):
        if self.Meta.model.objects.filter(email=value).exists():
            raise serializers.ValidationError(f"This email '{value}' is in use.")
        return value

    def validate_phone(self, value):
        if not value.isnumeric():
            raise serializers.ValidationError(f"This phone '{value}' is numeric.")
        elif len(value) not in [11]:
            raise serializers.ValidationError(f"This phone '{value}' is invalid size.")
        return value


class CreditorSerializer(PersonSerializerMixin):
    class Meta:
        model = CreditorModel
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        instance = self.Meta.model.objects.create(**validated_data)
        return instance


class DebtorSerializer(PersonSerializerMixin):
    class Meta:
        model = DebtorModel
        fields = "__all__"
