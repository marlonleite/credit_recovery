from django.db import models


class ContactAddress(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    address1 = models.TextField()
    address2 = models.TextField(blank=True)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    class Meta:
        db_table = "contact_address"

    def __str__(self):
        return f"{self.email} - {self.address1} - {self.zip_code} - {self.city}/{self.state}"


class Person(models.Model):
    document = models.CharField(min_length=11, max_length=14)
    name = models.CharField(max_length=100)
    contact_address = models.ForeignKey(ContactAddress, on_delete=models.CASCADE)

    class Meta:
        db_table = "person"

    def __str__(self):
        return f"{self.name} - {self.document}"
