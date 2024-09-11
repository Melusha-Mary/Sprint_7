import pytest
import requests
import makers
from data import Url


@pytest.fixture
def create_courier():
    login = makers.login_maker()
    password = makers.password_maker()
    name = makers.name_maker()
    create_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier_body)
    login_courier = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_courier_body)
    yield [create_courier_body, login_courier_body, login, password]
    requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{login_courier.json()['id']}')


@pytest.fixture
def make_courier_info():
    login = makers.login_maker()
    password = makers.password_maker()
    name = makers.name_maker()
    creation_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    yield [creation_courier_body, login_courier_body]
    login_courier = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_courier_body)
    requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{login_courier.json()['id']}')
