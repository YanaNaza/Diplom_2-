from json import loads
from helpers import *
from conftest import *

class TestCreateOrder:

    @allure.title('создание заказа с авторизацией пользователя')
    def test_create_order_authorized_user(self, create_user):
        user = create_user
        ingredients = generate_data_ingredient()
        order = Order()
        response = order.create_order(ingredients, user)
        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title('создание заказа неавторизованным пользователем')
    def test_create_order_unauthorized_user(self):
        ingredients = generate_data_ingredient()
        order = Order()
        response = order.create_order(ingredients)
        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title('создание заказа авторизованным пользователем со списком ингредиентов')
    def test_create_order_authorized_user_and_list(self, create_user):
        user = create_user
        ingredients = generate_data_ingredient()
        order = Order()
        response = order.create_order(ingredients, user)
        assert (response.status_code == 200) and (loads(response.text)['success'] == True)


    @allure.title('создание заказа авторизованным пользователем с пустым списком ингредиентов')
    def test_create_order_authorized_user_and_empty_list(self, create_user):
        user = create_user
        ingredients = []
        order = Order()
        response = order.create_order(ingredients, user)
        assert (response.status_code == 400) and (loads(response.text)['message'] == Message.NO_ONE_INGREDIENTS)


    @allure.title('создание заказа с неверным хешем ингредиентов')
    def test_create_order_authorized_user_and_bad_hash_ingredients(self, create_user):
        user = create_user
        ingredients = generate_data_ingredient()
        modified_ingredients = [ingredient + '_bad' for ingredient in ingredients]
        order = Order()
        response = order.create_order(modified_ingredients, user)
        assert response.status_code == 500
