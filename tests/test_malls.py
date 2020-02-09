from digeiz_api.models import Mall


class TestGetMalls:

    def test_get_malls(self, client, db, mall):
        response = client.get('/api/malls')
        response_json = response.get_json()

        assert response.status_code == 200
        assert len(response_json["malls"]) == 1

    def test_add_malls_valid(self, client, db, account, mall):

        data = {
            "name": "test_account 2",
            "account": account.id
        }

        response = client.post('/api/malls', json=data)
        malls_count = Mall.query.count()
        malls = Mall.query.all()

        assert response.status_code == 201
        assert malls_count == 2

        for mall in malls:
            assert mall.account_id == account.id

    def test_add_mall_not_valid(self, client, db, mall):

        data = {}
        response = client.post('/api/malls', json=data)
        assert response.status_code == 422


class TestGetMall:

    def test_get_mall_found(self, client, mall):
        response = client.get(f'/api/malls/{mall.id}')
        response_json = response.get_json()

        assert response.status_code == 200
        assert response_json["mall"]["id"] == 1

    def test_get_mall_not_found(self, client, mall):
        response = client.get(f'/api/malls/10000')

        assert response.status_code == 404


class TestDeleteMall:

    def test_delete_mall_valid(self, client, mall):
        response = client.delete(f'/api/malls/{mall.id}')
        malls = Mall.query.count()

        assert response.status_code == 204
        assert malls == 0

    def test_get_mall_not_found(self, client, mall):
        response = client.delete(f'/api/malls/10000')

        assert response.status_code == 404
