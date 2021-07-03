from random import randint

BASE_URL = "https://restful-booker.herokuapp.com"
AUTH = BASE_URL + "/auth"
BOOKING = BASE_URL + "/booking"
DELETE_BOOKING = f"https://restful-booker.herokuapp.com/booking/{randint(1,10)}"
PING = BASE_URL + "/ping"

