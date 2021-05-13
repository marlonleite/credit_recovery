import uuid

import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def create_superuser(db, django_user_model):
    def make_superuser(**kwargs):
        return django_user_model.objects.create_superuser(**kwargs)

    return make_superuser


@pytest.fixture
def admin_user(create_superuser):
    data = {
        "email": "admin@test.com",
        "username": "admin_user",
        "password": "test-password",
    }
    return create_superuser(**data)


@pytest.fixture
def strong_pass():
    return "test-password"


@pytest.fixture
def data():
    return {"value": "10.1", "creditor": 1, "debtors": [1, 2, 3]}


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False
