import requests
import pytest
import allure
from data import ResponseBody, Url, InfoForRegistration


class TestNewCourier:

    @allure.title('Тест на успешное создание нового курьера. Ручка:/api/v1/courier')
    def test_creation_courier_success(self, make_courier_info):
        registration = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=make_courier_info[0])
        assert registration.status_code == 201 and (registration.json() == ResponseBody.COURIER_CREATION_SUCCESS)

    @allure.title('Тест на отсутствие возможности создания двух одинаковых курьеров. Ручка:/api/v1/courier')
    def test_creation_courier_clone_error(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier[0])
        assert response.status_code == 409 and (response.json() == ResponseBody.COURIER_NAME_DONE)

    @allure.title('Тест на создание курьера, при отсутствии всех обязательных полей; нет: Login or Password. Ручка:/api/v1/courier')
    @pytest.mark.parametrize('data_setup', InfoForRegistration.reg_info)
    def test_creation_courier_without_info(self, data_setup):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', data_setup)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_REGISTRATION_NOT_INFO)
