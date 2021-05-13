from uuid import uuid4

from django.db import models

from customers.models import CreditorModel, DebtorModel


class CaseModel(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    creditor = models.ForeignKey(CreditorModel, on_delete=models.CASCADE)
    debtors = models.ManyToManyField(DebtorModel)

    class Meta:
        db_table = "case"

    def __str__(self):
        return f"{self.code} - {self.value}"
