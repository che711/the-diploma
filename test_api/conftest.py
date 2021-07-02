import pytest
from random import randint
import randomaizer
from test_api.headers import HEADERS
import requests
from test_api import api_urls
from json import dumps, loads
import json


@pytest.fixture()
def user_data():
    random_data = randomaizer.RandomData()
    random_name = random_data.generate_word(6)
    data = {
            "id": randint(1, 100),
            "username": 'admin',
            "firstName": random_name.title(),
            "lastName": random_name.title(),
            "email": "string@sad.com",
            "password": "password123",
            "phone": "123456789",
            "userStatus": randint(1, 100)
}
    return data

@pytest.fixture()
def create_booking():
    random_data = randomaizer.RandomData()
    random_name = random_data.generate_word(6)
    creare_booking = {
        "firstname": random_name.title(),
        "lastname": random_name.title(),
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": random_name.title()
    }
    return creare_booking

@pytest.fixture()
def partial_update():
    partial_update1 = {"firstname": "James", "lastname": "Brown"}
    return partial_update1

# @pytest.fixture()
# def create_cookie(user_data):
#     auth = requests.post(url=api_urls.AUTH, headers=HEADERS, data=dumps(user_data))
#     id = json.loads(auth.text)
#     a = f"token={id['token']}"
#     cookie = {"cookie": a}
#     return cookie