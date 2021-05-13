from customers.models import Person


class DebtorModel(Person):
    class Meta:
        db_table = "debtor"
