from json import loads

from conftest import *
from helpers import *


class TestCreateUser:
    @allure.title('создание уникального пользователя')
    def test_create_unique_user(self):
        user = User()
        response = user.create_user()
        user.delete_user()

        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title('создание пользователя, который уже зарегистрирован')
    def test_create_user_already_exists(self, create_user):
        response = create_user.create_user(create_user.data)

        assert (response.status_code == 403) and (loads(response.text)['message'] == Message.USER_ALREADY_EXISTS)

#
    @allure.title('регистрация пользователя с пустым полем email')
    def test_create_user_without_email(self):
        user = User()
        user.data = {**generate_data(), 'email': ''}
        response = user.create_user(user.data)

        assert (response.status_code == 403) and (loads(response.text)['message'] == Message.NO_ONE_FIELD)

    @allure.title('регистрация пользователя с пустым полем password')
    def test_create_user_without_password(self):
        user = User()
        user.data = {**generate_data(), 'password': ''}
        response = user.create_user(user.data)

        assert (response.status_code == 403) and (loads(response.text)['message'] == Message.NO_ONE_FIELD)


    @allure.title('регистрация пользователя с пустым полем name')
    def test_create_user_without_name(self):
        user = User()
        user.data = {**generate_data(), 'name': ''}
        response = user.create_user(user.data)

        assert (response.status_code == 403) and (loads(response.text)['message'] == Message.NO_ONE_FIELD)