class Url:
    SERVER_URL = 'https://stellarburgers.nomoreparties.site'

class EndPoints:
    GET_INGREDIENTS = '/api/ingredients'  # GET Получение данных об ингредиентах
    CREATE_ORDER = '/api/orders'  # POST создание заказа
    RESET_PASSWORD = '/api/password-reset/reset'  # POST сброс пароля
    CREATE_USER = '/api/auth/register'  #  POST регистрация пользователя
    LOGIN_USER = '/api/auth/login'    #  POST авторизация
    LOGOUT_USER = '/api/auth/logout'  #  POST выход
    DELETE_USER = '/api/auth/user'   # DELETE удаление пользователя
    UPDATE_TOKEN = '/api/auth/token'  # POST обновление токена
    GET_INFO_USER = '/api/auth/user'  # GET получение информации о пользователе
    UPDATE_USER = '/api/auth/user'   # PATCH  обновление данных о пользователе
    GET_ALL_ORDERS = '/api/orders'  # GET получение всех заказов - выводит 50 последних заказов
    ACCESS_TOKEN = 'Bearer '


class Message:
    LOGOUT = 'Successful logout'
    USER_DELETED = 'User successfully removed'
    PASSWORD_RESET_OK = 'Password successfully reset'
    USER_ALREADY_EXISTS = 'User already exists'
    NO_ONE_FIELD = 'Email, password and name are required fields'
    INVALID_LOGIN = 'email or password are incorrect'
    UNAUTHORIZED = 'You should be authorised'
    EMAIL_ALREADY_EXISTS = 'User with such email already exists'
    NO_ONE_INGREDIENTS = 'Ingredient ids must be provided'













