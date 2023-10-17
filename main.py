from user import User
from log import Loger, PATH
import pytest


@pytest.fixture
def data():
    test_name = 'Mike Tyson'
    test_id = 10
    test_level = 5
    return test_name, test_id, test_level


@pytest.fixture
def get_loger():
    return Loger(PATH)


@pytest.fixture
def invalid_name(data):
    test_name, test_id, test_level = data
    test_name = None
    return test_name, test_id, test_level


@pytest.fixture
def invalid_id(data):
    test_name, _, test_level = data
    test_id = -100
    return test_name, test_id, test_level


@pytest.fixture
def invalid_level(data):
    test_name, test_id, _ = data
    test_level = -100
    return test_name, test_id, test_level


@pytest.fixture
def invalid_level(data):
    test_name, test_id, _ = data
    test_level = -100
    return test_name, test_id, test_level


def test_user_creator(data):
    user = User(*data)
    assert user.__str__() == 'Mike Tyson, 10, 5'


def test_invalid_name_exception(invalid_name):
    with pytest.raises(ValueError, match=r'Имя должно быть текстового вида'):
        User(*invalid_name)


def test_invalid_id_exception(invalid_id):
    with pytest.raises(ValueError, match=r'Личный идентификатор должен быть целым числом'):
        User(*invalid_id)


def test_invalid_level_exception(invalid_level):
    with pytest.raises(ValueError, match=r'Уровень доступа должен быть целым числом от 1 до 7'):
        User(*invalid_level)


def test_users_identity(data):
    first_user = User(*data)
    second_user = User(*data)
    second_user.level = second_user.level - 1
    assert first_user == second_user


def test_users_non_identity(data):
    first_user = User(*data)
    second_user = User(*data)
    second_user.the_id = second_user.the_id + 1
    assert first_user != second_user


def test_user_auth(get_loger):
    assert get_loger.authorize(4, 'Mike Tyson') == 3


def test_add_user(get_loger):
    get_loger.authorize(4, 'Mike Tyson')
    with pytest.raises(Exception, match=r'Недостаточный уровень доступа'):
        get_loger.add_user('Dima Viktor', 7, 1)


if __name__ == '__main__':
    pytest.main(['-test'])