import pytest
from model_bakery import baker

from customers.models import DebtorModel


@pytest.mark.django_db
class TestDebtorEndpoints:
    @pytest.fixture(autouse=True)
    def setup_method_fixture(self, api_client, admin_user, data, strong_pass):
        self.endpoint = "/api/debtors/"
        self.client = api_client()
        self.data = data
        self.client.login(username=admin_user.username, password=strong_pass)

    def test_list(self):
        baker.make(DebtorModel, _quantity=3)
        response = self.client.get(self.endpoint)

        assert response.status_code == 200
        assert response.json()["count"] == 3
        assert len(response.json()["results"]) == 3

    def test_successful__create(self):
        response = self.client.post(self.endpoint, data=self.data, format="json")

        assert response.status_code == 201
        assert response.json()["name"] == "Test Name"
        assert response.json()["document"] == "62360965034"
        assert response.json()["email"] == "test@email.com"

    def test_unsuccessful__create_bad_data(self):
        data = {}
        response = self.client.post(self.endpoint, data=data, format="json")
        assert response.status_code == 400

    def test_unsuccessful__create_when_email_exists(self):
        baker.make(DebtorModel, email="test@email.com")
        response = self.client.post(self.endpoint, data=self.data, format="json")
        assert response.status_code == 400
        assert response.json() == {"email": ["This email 'test@email.com' is in use."]}

    def test_unsuccessful__create_when_document_exists(self):
        baker.make(DebtorModel, document="62360965034")
        response = self.client.post(self.endpoint, data=self.data, format="json")
        assert response.status_code == 400
        assert response.json() == {
            "document": ["This document '62360965034' is in use."]
        }

    def test_unsuccessful__create_when_phone_is_invalid(self):
        self.data["phone"] = "123456789"
        response = self.client.post(self.endpoint, data=self.data, format="json")
        assert response.status_code == 400
        assert response.json() == {"phone": ["This phone '123456789' is invalid size."]}

    def test_delete(self, mocker):
        model = baker.make(DebtorModel)
        response = self.client.delete(f"{self.endpoint}{model.id}/")

        DebtorModel.objects.filter(id=model.id).first()

        assert response.status_code == 204
