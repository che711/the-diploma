from random import randint

BASE_URL = "https://restful-booker.herokuapp.com"

AUTH = BASE_URL + "/auth"
BOOKING = BASE_URL + "/booking"
BOOKING_ID = BOOKING + f"/:{randint (1,20)}"
UPDATE_BOOKONG = "https://restful-booker.herokuapp.com/booking/:id"
PING = BASE_URL + "/ping"

