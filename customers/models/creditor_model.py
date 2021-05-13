from customers.models import Person


class CreditorModel(Person):
    class Meta:
        db_table = "creditor"
