from django.urls import path, include
from rest_framework import routers

from customers.views import CreditorViewSet, DebtorViewSet

router = routers.DefaultRouter()
router.register(r"creditors", CreditorViewSet)
router.register(r"debtors", DebtorViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
