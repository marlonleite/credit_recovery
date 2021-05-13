from django.db import models


class Address(models.Model):
    address = models.TextField()
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    class Meta:
        abstract = True


class Person(Address):
    document = models.CharField(max_length=14)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} - {self.document}"


class CreditorModel(Person):
    class Meta:
        db_table = "creditor"


class DebtorModel(Person):
    class Meta:
        db_table = "debtor"
