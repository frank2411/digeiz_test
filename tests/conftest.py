import pytest
from digeiz_api.app import create_app
from digeiz_api.models import db as _db
from digeiz_api.models import Account, Mall, Unit


@pytest.fixture
def app():
    app = create_app(testing=True)
    return app


@pytest.fixture
def client(app):
    yield app.test_client()


@pytest.fixture
def db(app):
    _db.app = app
    _db.session.expire_on_commit = False

    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def account(db):
    account = Account(name="test account")
    db.session.add(account)
    db.session.commit()
    return account


# @pytest.fixture
# def mall(db):
#     company = Company(name="Flowlity", email="@flowlity.com")
#     db.session.add(company)
#     db.session.commit()

#     return company


# @pytest.fixture
# def unit(db):
#     company = Company(name="Flowlity", email="@flowlity.com")
#     db.session.add(company)
#     db.session.commit()

#     return company
