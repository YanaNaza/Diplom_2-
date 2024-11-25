from json import loads
from data import Message
from conftest import *


class TestUpdateUser:
    @allure.title('изменение поля email авторизованного пользователя')
    def test_edit_email_authorized_user(self, create_user):
        user = create_user
        user.data = {**user.data, 'email': 'newskufbvhsilfnv@ya.ru'}

        response = user.update_info_about_user(user.data, user)

        assert (response.status_code == 200) and (loads(response.text)['user']['email'] == user.data["email"])


    @allure.title('изменение поля name авторизованного пользователя')
    def test_edit_name_authorized_user(self, create_user):
        user = create_user
        user.data = {**user.data, 'name': 'new'}
        response = user.update_info_about_user(user.data, user)

        assert (response.status_code == 200) and (loads(response.text)['user']['name'] == user.data["name"])

    @allure.title('изменение поля email НЕавторизованного пользователя')
    def test_edit_email_unauthorized_user(self, create_user):
        user = create_user
        user.data = {**user.data, 'email': 'new@ya.ru' }
        response = user.update_info_about_user(user.data)
        assert (response.status_code == 401) and (loads(response.text)['message'] == Message.UNAUTHORIZED)

    @allure.title('изменение поля name НЕавторизованного пользователя')
    def test_edit_name_unauthorized_user(self, create_user):
        user = create_user
        user.data = {**user.data, 'name': 'neweeeeeeee'}
        response = user.update_info_about_user(user.data)
        assert (response.status_code == 401) and (loads(response.text)['message'] == Message.UNAUTHORIZED)