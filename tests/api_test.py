import sys

sys.path.insert(1, '.')
from helpers import RetrieveJSONFromFile, \
                    RetrieveTextFromFile
import pymailbaby
from pymailbaby.exceptions import *
import pytest
from requests.auth import HTTPBasicAuth


class TestAPI:
    @pytest.fixture()
    def setUp(self):
        c = pymailbaby.Client(api_key="g4Q6dOI97ey2EblNCT2mheeMkTm1VxBBfMF8gRnA5MhZNV3uNsj5xGkZcygsTT6DNYqG267tMB24zHb1jFxOB9tkhBTR4ncz3iKxZWSvNx2Hvb8xbFQaQaybn28DzmZC",
                              order_id="21472")
        yield c

    # @pytest.fixture()
    # def setUpFailed(self):
    #     c = akauntingpy.Client("https://someakaunting-url/api",
    #                            "some-emailaddress@somewhere.com",
    #                            "aWrongPassWord",
    #                            1)
    #     yield c

    def test_init(self, setUp):
        c = setUp
        assert isinstance(c, pymailbaby.Client)
        assert c.baseurl == "https://api.mailbaby.net"

    def test_ping_success(self, setUp, requests_mock):
        c = setUp
        requests_mock.get(c.baseurl + '/ping',
                          json=RetrieveTextFromFile("data/pingSuccess.txt"),
                          status_code=200)
        data = c.ping()
        print(data)
        # The returned data should have status = ok
        assert data == 'Server is up and running'

    def test_ping_failed(self, setUp, requests_mock):
        c = setUp
        requests_mock.get(c.baseurl + '/ping',
                          json=RetrieveTextFromFile("data/pingFailure.txt"),
                          status_code=401)
        with pytest.raises(MissingPermission, match="Something is wrong"):
            data = c.ping()
            assert data['status_code'] == 401

    # def test_get_accounts(self, setUp, requests_mock):
    #     c = setUp
    #     requests_mock.get(c.url + "/accounts",
    #                       json=RetrieveJSONFromFile("data/GetAccountsList.json"))
    #     data = c.get_accounts(params={'page': 1, 'limit': 200})

    # def test_get_account_search_v2(self, setUp, requests_mock):
    #     c = setUp
    #     requests_mock.get(c.url + "/accounts?search=number%3A00-0000-0000000-00&params=page&params=limit&company_id=1",
    #                       json=RetrieveJSONFromFile("data/v2/GetAccountsSearch.json"))
    #     data = c.get_accounts(search="number:00-0000-0000000-00", params={'page': 1, 'limit': 200})

    # def test_get_account_search_v3(self, setUp, requests_mock):
    #     c = setUp
    #     requests_mock.get(c.url + "/accounts?search=number%3A00-0000-0000000-00&params=page&params=limit&company_id=1",
    #                       json=RetrieveJSONFromFile("data/v3/GetAccountsSearch.json"))
    #     data = c.get_accounts(search="number:00-0000-0000000-00", params={'page': 1, 'limit': 200})
        
    # def test_get_account_search_not_found_v2(self, setUp, requests_mock):
    #     c = setUp
    #     requests_mock.get(c.url + "/accounts?search=number%3Aarandomvalue&company_id=1",
    #                       json=RetrieveJSONFromFile("data/v2/GetAccountsSearchNotFound.json"))
    #     with pytest.raises(AccountNotFound):
    #         data = c.get_accounts(search="number:arandomvalue")

    # def test_get_account_search_not_found_v3(self, setUp, requests_mock):
    #     c = setUp
    #     requests_mock.get(c.url + "/accounts?search=number%3Aarandomvalue&company_id=1",
    #                       json=RetrieveJSONFromFile("data/v3/GetAccountsSearchNotFound.json"))
    #     with pytest.raises(AccountNotFound):
    #         data = c.get_accounts(search="number:arandomvalue")
            
    # def test_create_transaction_income_success(self, setUp, requests_mock,
    #                                            transaction_type='income',  # Payment method type
    #                                            account_id=2,  # Account ID to assign
    #                                            category_id=3,  # Category ID to assign
    #                                            contact_id=None,  # Contact ID/Client to assign
    #                                            paid_at="2022-05-15",  # Date of expense/transfer or income
    #                                            reference=None,  # Reference for the payment
    #                                            payment_method="bank_transfer",  # Payment method
    #                                            currency_code="NZD",  # Currency code
    #                                            currency_rate=1,  # Currency rate
    #                                            amount="25.00",  # Amount received/paid
    #                                            ):
    #     c = setUp
    #     requests_mock.post(c.url + "/transactions",
    #                        json=RetrieveJSONFromFile("data/CreateTransactionIncomeSuccess.json"),
    #                        status_code=201)
    #     data = c.create_transaction(transaction_type=transaction_type,
    #                                 account_id=account_id,
    #                                 category_id=category_id,
    #                                 paid_at=paid_at,
    #                                 contact_id=contact_id,
    #                                 payment_method=payment_method,
    #                                 reference=reference,
    #                                 currency_code=currency_code,
    #                                 currency_rate=currency_rate,
    #                                 amount=amount,
    #                                 description="Some description of the transaction"
    #                                 )

    # def test_create_transaction_income_default_currency_success(self, setUp, requests_mock,
    #                                                             transaction_type='income',  # Payment method type
    #                                                             account_id=2,  # Account ID to assign
    #                                                             category_id=3,  # Category ID to assign
    #                                                             contact_id=None,  # Contact ID/Client to assign
    #                                                             paid_at="2022-05-15",
    #                                                             # Date of expense/transfer or income
    #                                                             reference=None,  # Reference for the payment
    #                                                             payment_method="bank_transfer",  # Payment method
    #                                                             amount="25.00",  # Amount received/paid
    #                                                             ):
    #     c = setUp
    #     requests_mock.post(c.url + "/transactions",
    #                        json=RetrieveJSONFromFile("data/CreateTransactionIncomeSuccess.json"),
    #                        status_code=201)
    #     data = c.create_transaction(transaction_type=transaction_type,
    #                                 account_id=account_id,
    #                                 category_id=category_id,
    #                                 paid_at=paid_at,
    #                                 contact_id=contact_id,
    #                                 payment_method=payment_method,
    #                                 reference=reference,
    #                                 amount=amount,
    #                                 description="Some description of the transaction"
    #                                 )

    # def test_create_transaction_income_failed(self, setUp, requests_mock,
    #                                           contact_id=None,  # Contact ID/Client to assign
    #                                           reference=None,  # Reference for the payment
    #                                           currency_code="NZD",  # Currency code
    #                                           currency_rate=1,  # Currency rate
    #                                           amount="25.00",  # Amount received/paid
    #                                           ):
    #     c = setUp
    #     requests_mock.post(c.url + "/transactions",
    #                        json=RetrieveJSONFromFile("data/CreateTransactionIncomeFailed.json"),
    #                        status_code=422)
    #     with pytest.raises(InvalidData, match="The given data was invalid.*"):
    #         data = c.create_transaction(contact_id=contact_id,
    #                                     reference=reference,
    #                                     currency_code=currency_code,
    #                                     currency_rate=currency_rate,
    #                                     amount=amount,
    #                                     description="Some description of the transaction"
    #                                     )

    # def test_create_transaction_expense_success(self, setUp, requests_mock):
    #     c = setUp
    #     requests_mock.post(c.url + "/transactions?search=type%3Aexpense&type=expense&account_id=3&category_id=4&paid_at=2022-05-16&payment_method=Bank+Transfer&currency_code=NZD&currency_rate=1&amount=100.0&description=Some+expenditures&company_id=1",
    #                        json=RetrieveJSONFromFile("data/CreateTransactionExpenseSuccess.json"),
    #                        status_code=201)
    #     data = c.create_transaction(transaction_type="expense",
    #                                 amount=100.00,
    #                                 account_id=3,
    #                                 paid_at="2022-05-16",
    #                                 currency_rate=1,
    #                                 currency_code="NZD",
    #                                 payment_method="Bank Transfer",
    #                                 category_id="4",
    #                                 description="Some expenditures"
    #                                 )


    # def test_create_transfer_success(self, setUp, requests_mock):
    #     c = setUp
    #     requests_mock.post(c.url + "/transfers",
    #                        json=RetrieveJSONFromFile("data/CreateTransferSuccess.json"),
    #                        status_code=201)
    #     data = c.create_transfer(   amount=100.00,
    #                                 account_id=3,
    #                                 paid_at="2022-05-16",
    #                                 currency_rate=1,
    #                                 currency_code="NZD",
    #                                 payment_method="Bank Transfer",
    #                                 category_id="4",
    #                                 description="Some expenditures"
    #                                 )