import pytest
from json import dumps
import requests
from random import randint
from test_api import api_urls
from test_api.headers import HEADERS
import randomaizer

@pytest.fixture()
def user_data():
    random_data = randomaizer.RandomData()
    random_name = random_data.generate_word(6)
    random_word = random_data.generate_word(6)

    data = {
            "id": randint(1, 100),
            "username": random_name,
            "firstName": random_word,
            "lastName": random_word,
            "email": "string@sad.com",
            "password": "123456789",
            "phone": "123456789",
            "userStatus": randint(1, 100)
}
    return data


@pytest.fixture()
def user(user_data):
    user_response = requests.post(
        url=api_urls.USER, headers=HEADERS, data=dumps(user_data)
    )
    assert user_response.status_code == 200

    yield user_data

    delete_user_response = requests.delete(url=api_urls.USER_NAME.format(username=user_data["username"]),
        headers=HEADERS
        )
    assert delete_user_response.status_code == 200