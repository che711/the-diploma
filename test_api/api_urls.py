from random import randint

BASE_URL = "https://restful-booker.herokuapp.com"

AUTH = BASE_URL + "/auth"  # https://restful-booker.herokuapp.com/auth
BOOKING = BASE_URL + "/booking"  #  https://restful-booker.herokuapp.com/booking
BOOKING_ID = BOOKING + f"/:id"  # https://restful-booker.herokuapp.com/booking/:id
DELETE_BOOKING = "https://restful-booker.herokuapp.com/booking/1"
PING = BASE_URL + "/ping"  # https://restful-booker.herokuapp.com/ping

