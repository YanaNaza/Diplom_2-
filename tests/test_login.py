from json import loads
from data import Message
from conftest import *

class TestLoginUser:
    @allure.title('успешная регистрация при указании логина и пароля зарегистрированного пользователя')
    def test_login_authorized_user(self, create_user):
        user = create_user
        response = user.login_user(user.data)

        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title('ошибка 401 при указании неверного логина зарегистрированного пользователя')
    def test_login_authorized_user_with_incorrect_email(self, create_user):
        user = create_user
        user.data = {**user.data, 'email': 'newskufbvhsilfnv@y'}
        response = user.login_user(user.data)

        assert (response.status_code == 401) and (loads(response.text)['message'] == Message.INVALID_LOGIN)

    @allure.title('ошибка 401 при указании неверного пароля зарегистрированного пользователя')
    def test_login_authorized_user_with_incorrect_password(self, create_user):
        user = create_user
        user.data = {**user.data, 'password': 'nono'}
        response = user.login_user(user.data)

        assert (response.status_code == 401) and (loads(response.text)['message'] == Message.INVALID_LOGIN)