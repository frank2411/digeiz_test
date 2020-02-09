import pytest
from digeiz_api.app import create_app
from digeiz_api.models.db import db as _db
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


@pytest.fixture
def mall(db, account):
    mall = Mall(name="test mall", account_id=account.id)
    db.session.add(mall)
    db.session.commit()
    return mall


@pytest.fixture
def unit(db, mall):
    unit = Unit(name="test unit", mall_id=mall.id)
    db.session.add(unit)
    db.session.commit()
    return mall
