import allure
import pytest
from helpers import User


@pytest.fixture(scope="function")
@allure.title('создаем пользователя c данными для удаления после завершения работы')
def create_user():
    user = User()
    user.create_user()
    yield user
    user.delete_user()