from django.db import models

from customers.models import Address


class Person(Address):
    document = models.CharField(max_length=14)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} - {self.document}"
