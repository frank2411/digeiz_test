from digeiz_api.models import Account


class TestGetAccounts:

    def test_get_accounts(self, client, db, account):
        response = client.get('/api/accounts')
        response_json = response.get_json()

        assert response.status_code == 200
        assert len(response_json["accounts"]) == 1

    def test_add_account_valid(self, client, db, account):

        data = {
            "name": "test_account 2"
        }

        response = client.post('/api/accounts', json=data)
        accounts = Account.query.count()

        assert response.status_code == 201
        assert accounts == 2

    def test_add_account_not_valid(self, client, db, account):

        data = {}
        response = client.post('/api/accounts', json=data)
        assert response.status_code == 422


class TestGetAccount:

    def test_get_account_found(self, client, account):
        response = client.get(f'/api/accounts/{account.id}')
        response_json = response.get_json()

        assert response.status_code == 200
        assert response_json["account"]["id"] == 1

    def test_get_account_not_found(self, client, account):
        response = client.get(f'/api/accounts/10000')

        assert response.status_code == 404


class TestDeleteAccount:

    def test_delete_account_valid(self, client, account):
        response = client.delete(f'/api/accounts/{account.id}')
        accounts = Account.query.count()

        assert response.status_code == 204
        assert accounts == 0

    def test_get_account_not_found(self, client, account):
        response = client.delete(f'/api/accounts/10000')

        assert response.status_code == 404
