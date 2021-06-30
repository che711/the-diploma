import requests
from test_api import api_urls
from test_api.headers import HEADERS, ACCEPT,HEADERS_TWO
from json import dumps, loads
import json

#  pytest -s -vv --html=report.html test_test.py

def test_booking_update(create_booking, user_data, partial_update):
    '''Updates a current booking'''
    ids = []
    auth = requests.post(url=api_urls.AUTH, headers=HEADERS, data=dumps(user_data))
    id = json.loads(auth.text)
    token = {"token": f"{id['token']}"}
    print("\n\t", auth.status_code, "\n\t", auth.text, "\n\t", id['token'], )
    creare_booking_post = requests.post(url=api_urls.BOOKING, headers=HEADERS, params=token, data=dumps(create_booking))
    print("\n\t", creare_booking_post.status_code, "\n\t", creare_booking_post.json())
    dic = creare_booking_post.json()
    for key, value in dic.items():
        ids.append(value)
    print(ids)
    link = f"https://restful-booker.herokuapp.com/booking/{ids[0]}"
    print("\n\t", link)
    api_param = {
        "token": f"id['token']",
        "username": "admin",
        "password": "password123"
    }
    booking_update = requests.patch(url=link, headers=HEADERS, params=api_param, data=dumps(partial_update))
    print("\n\tresponse.url:\n{}\n\n".format(booking_update.url))
    print("\n\t", booking_update.status_code, "\n\t", booking_update.headers)
    assert booking_update.status_code == 200, 'Falling'

