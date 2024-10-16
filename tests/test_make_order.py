import pytest
import requests
import allure

from data import Url, InfoForOrder, Flags


class TestCreationOrder:

    @allure.title('Тест на успешное создание заказа с разными вариантами цветов. Ручка:/api/v1/orders')
    @pytest.mark.parametrize('scooter_color', InfoForOrder.scooter_color)
    def test_create_order_with_colors(self, scooter_color):
        order_info = InfoForOrder.order_info
        order_info['color'] = scooter_color
        order = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_info)
        assert order.status_code == 201 and Flags.SUCCESSFUL_ORDER_CREATION in order.json()
        requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{order.json()['track']}')
