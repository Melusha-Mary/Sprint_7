import requests
import allure
import makers

from data import Url, ResponseBody


class TestLoginCourier:

    @allure.title('Тест на успешный вход курьера в систему, указав полную регистрационную информацию. Ручка:/api/v1/courier/login')
    def test_successful_courier_login(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=create_courier[1])
        courier_id = response.json()
        assert response.status_code == 200 and courier_id != ''

    @allure.title('Тесто на вход курьера в систему с незарегистрированной учетной записью. Ручка:/api/v1/courier/login')
    def test_unregistered_courier_login(self):
        login_info = {'login': makers.login_maker(), 'password': makers.password_maker()}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', login_info)
        assert response.status_code == 404 and (response.json() == ResponseBody.COURIER_ACCOUNT_NOT_FOUND)

    @allure.title('Тест на вход курьера в систему с пустым паролем. Ручка:/api/v1/courier/login')
    def test_courier_login_without_password(self, create_courier):
        info_response = {'login': create_courier[2], 'password': ''}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=info_response)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_LOGIN_NOT_INFO)

    @allure.title('Тест на вход курьера в систему с пустым логином. Ручка:/api/v1/courier/login')
    def test_courier_login_without_login(self, create_courier):
        info_response = {'login': '', 'password': create_courier[3]}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=info_response)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_LOGIN_NOT_INFO)
