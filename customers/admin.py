from django.contrib import admin

from customers.models import CreditorModel, DebtorModel

admin.site.register(CreditorModel)
admin.site.register(DebtorModel)
