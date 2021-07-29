import requests
from test_api import api_urls
from test_api.headers import HEADERS
from json import dumps
import json

#  pip install -r requirements.txt
#  pytest -s -vv --alluredir=results tests_api.py

def test_auth(user_data):
    '''Creating a new user'''
    auth = requests.post(url=api_urls.AUTH, headers=HEADERS,  data=dumps(user_data))
    assert auth.status_code == 200, 'Auth does not work'

def test_booking(create_booking):
    '''Returns a specific booking based upon the booking id provided.'''
    ids = []
    booking_get = requests.get(url=api_urls.BOOKING, headers=HEADERS)
    dic = booking_get.json()
    for keys in dic:
        for key, value in keys.items(): ids.append(value)
    link = f"https://restful-booker.herokuapp.com/booking/{ids[0]}"
    booking_id_get = requests.get(url=link, headers=HEADERS, data=dumps(create_booking))
    assert booking_id_get.status_code == 200, 'Reservation by id does not work'

def test_bookinglbs():
    '''
    Returns the ids of all the bookings that exist within the API.
    Can take optional query strings to search and return a subset of booking ids.
    '''
    booking_get = requests.get(url=api_urls.BOOKING, headers=HEADERS)
    assert booking_get.status_code == 200, 'Reservation does not work'

def test_create_booking(create_booking):
    '''Creates a new booking in the API'''
    create_booking_post = requests.post(url=api_urls.BOOKING, headers=HEADERS,  data=dumps(create_booking))
    assert create_booking_post.status_code == 200, 'Creating a reservation by id does not work'

def test_booking_update(create_booking, user_data):
    '''Updates a current booking'''
    ids = []
    auth = requests.post(url=api_urls.AUTH, headers=HEADERS, data=dumps(user_data))
    id = json.loads(auth.text)
    make_cookie = f"token={id['token']}"
    cookie = {"cookie": make_cookie}
    creare_booking_post = requests.post(url=api_urls.BOOKING, headers=HEADERS,  data=dumps(create_booking))
    dic = creare_booking_post.json()
    for key, value in dic.items(): ids.append(value)
    link = f"https://restful-booker.herokuapp.com/booking/{ids[0]}"
    booking_update = requests.patch(url=link, headers=cookie, data=dumps(create_booking))
    assert booking_update.status_code == 200, 'Update does not work'


def test_partial_update_booking(create_booking, user_data):
    '''Updates a current booking with a partial payload'''
    ids = []
    auth = requests.post(url=api_urls.AUTH, headers=HEADERS, data=dumps(user_data))
    cookie_value = f"token={json.loads(auth.text)['token']}"
    cookie = {"cookie": cookie_value}
    creare_booking_post = requests.post(url=api_urls.BOOKING, headers=HEADERS,  data=dumps(create_booking))
    dic = creare_booking_post.json()
    for key, value in dic.items(): ids.append(value)
    link = f"https://restful-booker.herokuapp.com/booking/{ids[0]}"
    partial_update_booking = requests.patch(url=link, headers=cookie, data=dumps(create_booking))
    assert partial_update_booking.status_code == 200, 'Partial update by id does not work'

def test_delete_booking(user_data):
    '''Delete_booking'''
    auth = requests.post(url=api_urls.AUTH, headers=HEADERS, data=dumps(user_data))
    id = json.loads(auth.text)
    a = f"token={id['token']}"
    cookie = {"cookie": a}
    booking_delete = requests.delete(url=api_urls.DELETE_BOOKING, headers=cookie)
    assert booking_delete.status_code == 201, 'Deleting does not work'

def test_ping():
    '''A simple health check endpoint to
    confirm whether the API is up and running'''
    ping = requests.get(url=api_urls.PING)
    assert ping.status_code == 201, 'The health API is not working'




