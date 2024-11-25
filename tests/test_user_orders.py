from json import loads

from helpers import *
from conftest import *


class TestGetOrder:
    @allure.title('при запросе заказов авторизованным пользователем выводится список заказов')
    def test_get_authorized_user_order(self, create_user):
        user = create_user
        order = Order()
        ingredients = generate_data_ingredient()
        order.create_order(ingredients, user)
        response = user.get_order(user)

        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title('при запросе заказов НЕавторизованным пользователем возвращается 401 ошибка')
    def test_get_unauthorized_user_order(self):
        user = User()
        response = user.get_order()

        assert (response.status_code == 401) and (loads(response.text)['message'] == Message.UNAUTHORIZED)