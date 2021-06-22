import requests
from json import loads, dumps
from test_api import api_urls
from test_api.headers import HEADERS

def test_user_crud(user_data):
    user_response = requests.post(
        url=api_urls.USER, headers=HEADERS, data=dumps(user_data)
    )
    assert user_response.status_code == 200
    get_user_response = requests.get(
        url=api_urls.USER_NAME.format(username=user_data["username"]),
        headers=HEADERS
    )
    assert get_user_response.status_code == 200, 'not OK'
    assert get_user_response.json()["id"] == user_data["id"]
    update_data = {"email": "updated@sad.com"}
    updated_user_data = {**user_data, **update_data}
    updated_response = requests.put(
        url=api_urls.USER_NAME.format(username=user_data["username"]),
        headers=HEADERS,
        data=dumps(updated_user_data)
    )
    assert updated_response.status_code == 200
    get_updated_user = requests.get(
        url=api_urls.USER_NAME.format(username=user_data["username"]),
        headers=HEADERS
    )
    assert get_updated_user.status_code == 200, 'not OK v.2'
    assert get_updated_user.json()["email"] == update_data["email"]
    delete_user_response = requests.delete(
        url=api_urls.USER_NAME.format(username=user_data["username"]),
        headers=HEADERS
    )
    assert delete_user_response.status_code == 200
    get_deleted_user = requests.get(
        url=api_urls.USER_NAME.format(username=user_data["username"]),
        headers=HEADERS
    )
    assert get_deleted_user.status_code == 404


def test_auth(user):
    login_response = requests.get(
        url=api_urls.LOGIN,
        headers=HEADERS,
        params={"username": user["username"], "password": user["password"]}
    )
    assert login_response.status_code == 200
    assert "logged in user session" in login_response.json()["message"]
    logout_response = requests.get(
        url=api_urls.LOGOUT,
        headers=HEADERS
    )
    assert logout_response.status_code == 200
    assert logout_response.json()["message"] == "ok"
