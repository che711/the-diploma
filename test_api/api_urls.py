from random import randint

BASE_URL = "https://restful-booker.herokuapp.com"

AUTH = BASE_URL + "/auth"  # https://restful-booker.herokuapp.com/auth
BOOKING = BASE_URL + "/booking"  #  https://restful-booker.herokuapp.com/booking
BOOKING_ID = BOOKING + f"/1"  # https://restful-booker.herokuapp.com/booking/:id
DELETE_BOOKING = f"https://restful-booker.herokuapp.com/booking/{randint(1,10)}"
PING = BASE_URL + "/ping"  # https://restful-booker.herokuapp.com/ping

