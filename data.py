import makers


class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    CREATE_COURIER = 'api/v1/courier'
    COURIER_LOGIN = 'api/v1/courier/login'
    COURIER_DELETE = 'api/v1/courier/'
    CREATE_ORDER = 'api/v1/orders'
    ORDER_LIST = 'api/v1/orders'
    ORDER_CANCEL = 'api/v1/orders/cancel?track='
    TRACK_ORDER = '/api/v1/orders/track?t='


class InfoForOrder:
    order_info = {"firstName": "Mary",
                  "lastName": "Leshukova",
                  "address": "Sovetskaya 45",
                  "metroStation": 5,
                  "phone": "+79876543210",
                  "rentTime": 2,
                  "deliveryDate": "2024-09-12",
                  "comment": "очень ждем"
                  }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]


class InfoForRegistration:
    reg_info = [{'password': makers.password_maker(), 'first_name': makers.name_maker()},
                {'login': makers.login_maker(), 'first_name': makers.name_maker()}]


class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_DONE = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}  #
    COURIER_REGISTRATION_NOT_INFO = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    COURIER_LOGIN_NOT_INFO = {'code': 400, 'message': 'Недостаточно данных для входа'}


class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_ORDER_LIST = 'orders'
