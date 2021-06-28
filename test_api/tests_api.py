import requests
from test_api import api_urls
from test_api.headers import HEADERS
from json import dumps, loads

#  pytest -s -vv --html=report.html tests_api.py

def test_auth(user_data):
    '''Creating a new user'''
    auth = requests.post(url=api_urls.AUTH, headers=HEADERS, data=dumps(user_data))
    print("\n\t", auth.status_code, "\t", auth.text)
    assert auth.status_code == 200, 'Falling'

def test_booking():
    '''Returns a specific booking based upon the booking id provided.'''
    booking_id_get = requests.get(url=api_urls.BOOKING, headers=HEADERS, )
    print("\n\t", booking_id_get.status_code, "\t", booking_id_get.headers)
    assert booking_id_get.status_code == 200, 'Falling'

def test_bookinglbs():
    '''
    Returns the ids of all the bookings that exist within the API.
    Can take optional query strings to search and return a subset of booking ids.
    '''
    booking_get = requests.get(url=api_urls.BOOKING, headers=HEADERS, )
    print("\n\t", booking_get.status_code, "\t", booking_get.text)
    assert booking_get.status_code == 200, 'Falling'
    # asdf = list(booking_get)
    # print("\n\t", asdf[0],[0])


def test_creare_booking(creare_booking):
    '''Creates a new booking in the API'''
    creare_booking_post = requests.post(url=api_urls.BOOKING, headers=HEADERS,  data=dumps(creare_booking))
    print("\n\t", creare_booking_post.status_code, "\t", creare_booking_post.text)
    assert creare_booking_post.status_code == 200, 'Falling'


def test_booking_update(creare_booking):
    '''Updates a current booking'''
    booking_update = requests.put(url=api_urls.UPDATE_BOOKONG, headers=HEADERS, data=dumps(creare_booking))
    print("\n\t", booking_update.status_code, "\t", booking_update.headers)
    assert booking_update.status_code == 200, 'Falling'


def test_partial_update_booking(creare_booking):
    '''Updates a current booking with a partial payload'''
    partial_update = requests.put(url=api_urls.BOOKING, headers=HEADERS, data=dumps(creare_booking))
    print("\n\t", partial_update.status_code, "\n\t", partial_update.headers)
    assert partial_update.status_code == 200, 'Falling'


def test_delete_booking():
    '''
    Returns the ids of all the bookings that exist within the API.
    Can take optional query strings to search and return a subset of booking ids.
    '''
    booking_delete = requests.delete(url=api_urls.DELETE_BOOKING, headers=HEADERS,)
    print("\n\t", booking_delete.status_code, "\t", booking_delete.headers)
    assert booking_delete.status_code == 201, 'Falling'

def test_ping():
    '''A simple health check endpoint to confirm whether the API is up and running'''
    ping = requests.get(url=api_urls.PING)
    print("\n\t", ping.status_code, "\t", ping.text)
    assert ping.status_code == 201, 'Falling'




