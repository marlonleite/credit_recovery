import pytest
from model_bakery import baker

from cases.models import CaseModel
from cases.tests.conftest import is_valid_uuid
from customers.models import CreditorModel, DebtorModel


@pytest.mark.django_db
class TestCaseEndpoints:
    @pytest.fixture(autouse=True)
    def setup_method_fixture(self, api_client, admin_user, data, strong_pass):
        self.endpoint = "/api/cases/"
        self.client = api_client()
        self.data = data
        self.client.login(username=admin_user.username, password=strong_pass)

        baker.make(CreditorModel, id=1, name="Creditor Test1")
        baker.make(DebtorModel, id=1, name="Debtor Test1")
        baker.make(DebtorModel, id=2, name="Debtor Test2")
        baker.make(DebtorModel, id=3, name="Debtor Test3")

    def test_list(self):
        baker.make(CaseModel, _quantity=3)
        response = self.client.get(self.endpoint)

        assert response.status_code == 200
        assert response.json()["count"] == 3
        assert len(response.json()["results"]) == 3

    def test_successful__create(self):
        response = self.client.post(self.endpoint, data=self.data, format="json")
        assert response.status_code == 201
        assert response.json()["creditor"]["name"] == "Creditor Test1"
        assert len(response.json()["debtors"]) == 3
        assert response.json()["value"] == "10.10"
        assert is_valid_uuid(response.json()["code"])

    def test_unsuccessful__create_bad_data(self):
        data = {}
        response = self.client.post(self.endpoint, data=data, format="json")
        assert response.status_code == 400

    def test_unsuccessful__create_when_value_is_invalid(self):
        self.data["value"] = "10,20"
        response = self.client.post(self.endpoint, data=self.data, format="json")
        assert response.status_code == 400
        assert response.json() == {"value": ["A valid number is required."]}

    def test_unsuccessful__create_when_missing_required_field(self):
        del self.data["creditor"]
        response = self.client.post(self.endpoint, data=self.data, format="json")
        assert response.status_code == 400
        assert response.json() == {"creditor": ["This field is required."]}

    def test_unsuccessful__create_when_empty_debtors_list(self):
        self.data["debtors"] = []
        response = self.client.post(self.endpoint, data=self.data, format="json")
        assert response.status_code == 400
        assert response.json() == {"debtors": ["This list may not be empty."]}

    def test_successful__update(self):
        model = baker.make(CaseModel, value="10.00")
        data = {"value": "200.50"}
        response = self.client.patch(
            f"{self.endpoint}{model.code}/", data=data, format="json"
        )
        assert response.status_code == 200
        assert response.json()["value"] == "200.50"

    def test_delete(self, mocker):
        model = baker.make(CaseModel)
        response = self.client.delete(f"{self.endpoint}{model.code}/")
        case = CaseModel.objects.filter(code=model.code).first()
        assert response.status_code == 204
        assert case is None
