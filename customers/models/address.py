from django.db import models


class Address(models.Model):
    address = models.TextField()
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    class Meta:
        abstract = True
