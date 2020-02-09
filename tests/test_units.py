from digeiz_api.models import Unit


class TestGetUnits:

    def test_get_units(self, client, db, unit):
        response = client.get('/api/units')
        response_json = response.get_json()

        assert response.status_code == 200
        assert len(response_json["units"]) == 1

    def test_add_unit_valid(self, client, db, mall, unit):

        data = [{
            "name": "test_unit 2",
            "mall": mall.id
        }]

        response = client.post('/api/units', json=data)
        units_count = Unit.query.count()
        units = Unit.query.all()

        assert response.status_code == 201
        assert units_count == 2

        for unit in units:
            assert unit.mall_id == mall.id

    def test_add_units_valid(self, client, db, mall, unit):

        data = [
            {
                "name": "test_unit 2",
                "mall": mall.id
            },
            {
                "name": "test_unit 3",
                "mall": mall.id
            },
        ]

        response = client.post('/api/units', json=data)
        units_count = Unit.query.count()
        units = Unit.query.all()

        assert response.status_code == 201
        assert units_count == 3

        for unit in units:
            assert unit.mall_id == mall.id

    def test_add_unit_not_valid(self, client, db, unit):

        data = {}
        response = client.post('/api/units', json=data)
        assert response.status_code == 422


class TestGetUnit:

    def test_get_unit_found(self, client, unit):
        response = client.get(f'/api/units/{unit.id}')
        response_json = response.get_json()

        assert response.status_code == 200
        assert response_json["unit"]["id"] == 1

    def test_get_unit_not_found(self, client, unit):
        response = client.get(f'/api/units/10000')

        assert response.status_code == 404


class TestDeleteUnit:

    def test_delete_unit_valid(self, client, unit):
        response = client.delete(f'/api/units/{unit.id}')
        units = Unit.query.count()

        assert response.status_code == 204
        assert units == 0

    def test_get_unit_not_found(self, client, unit):
        response = client.delete(f'/api/units/10000')

        assert response.status_code == 404
