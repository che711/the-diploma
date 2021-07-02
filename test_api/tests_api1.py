import requests
from test_api import api_urls
from test_api.headers import HEADERS, ACCEPT,HEADERS_TWO
from json import dumps, loads
import json

#  pytest -s -vv --html=report.html tests_api1.py


def test_delete_booking(user_data):
    '''Delete_booking'''
    auth = requests.post(url=api_urls.AUTH, headers=HEADERS, data=dumps(user_data))
    id = json.loads(auth.text)
    a = f"token={id['token']}"
    cookie = {"cookie": a}
    booking_delete = requests.delete(url=api_urls.DELETE_BOOKING, headers=cookie)
    print("\n\t", booking_delete.status_code, "\t", booking_delete.text)
    print(api_urls.DELETE_BOOKING)
    assert booking_delete.status_code == 201, 'Falling'