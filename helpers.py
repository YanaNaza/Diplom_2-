import allure
import random
from random import randint
import string
import requests
from data import *


@allure.step('генерация рандомной строки с буквами в нижнем регистре')
def random_string(length):
    return (f"{''.join(random.choice(string.ascii_lowercase) for i in range(length))}")


@allure.step('генерация данных пользователя')
def generate_data():
    user_data = {
        'email': random_string(10) + '@ya.ru',
        'name': random_string(10),
        'password': random_string(10)
    }
    return user_data

@allure.step('генерация рандомных ингредиенты')
def generate_data_ingredient():
    response = requests.get(Url.SERVER_URL + EndPoints.GET_INGREDIENTS)
    ingredients = [ingredient['_id'] for ingredient in response.json()['data']]

    return ingredients[: randint(1, len(ingredients))]


class User:
    def __init__(self):
        self.data = {'accessToken': '',
                     'email': '',
                     'password': '',
                     'name': ''}

    @allure.step('регистрация пользователя')
    def create_user(self, user_data=None):
        if user_data is None:
            self.data.update(generate_data())


        response = requests.post(Url.SERVER_URL + EndPoints.CREATE_USER, data=self.data)


        if response.status_code == 200:
            self.data['accessToken'] = response.json()['accessToken']

        return response

    @allure.step('авторизация пользователя')
    def login_user(self, user_data):

        response = requests.post(Url.SERVER_URL + EndPoints.LOGIN_USER, data=user_data)

        return response


    @allure.step('обновление данных о пользователе')
    def update_info_about_user(self, user_data, user=None):
        if user:
            headers = {'Authorization': self.data['accessToken']}
        else:
            headers = ''

        response = requests.patch(Url.SERVER_URL + EndPoints.UPDATE_USER, data=user_data, headers=headers)

        return response


    @allure.step('удаление пользователя')
    def delete_user(self):
        if self.data['accessToken']:
            headers = {'Authorization': self.data['accessToken']}

            response = requests.delete(Url.SERVER_URL + EndPoints.DELETE_USER, headers=headers)

            return response


    @allure.step('получение списка заказов')
    def get_order(self, user=None):
        if user:
            headers = {'Authorization': self.data['accessToken']}
        else:
            headers = ''

        response = requests.get(Url.SERVER_URL + EndPoints.GET_ALL_ORDERS, headers=headers)

        return response


class Order:
    @allure.step('создание заказа')
    def create_order(self, ingredients, user=None):
        if user:
            headers = {'Authorization': user.data['accessToken']}
        else:
            headers = ''
        data = {'ingredients': ingredients}

        response = requests.post(Url.SERVER_URL + EndPoints.CREATE_ORDER, headers=headers, data=data)

        return response




