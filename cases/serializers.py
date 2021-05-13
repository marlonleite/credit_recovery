from rest_framework import serializers

from cases.models import CaseModel


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseModel
        fields = "__all__"
        extra_kwargs = {"debtors": {"required": False}}

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["creditor"] = {
            "id": instance.creditor.id,
            "name": instance.creditor.name,
            "document": instance.creditor.document,
        }
        ret["debtors"] = []
        for v in instance.debtors.all():
            ret["debtors"].append(
                {
                    "id": v.id,
                    "name": v.name,
                    "document": v.document,
                }
            )
        return ret
