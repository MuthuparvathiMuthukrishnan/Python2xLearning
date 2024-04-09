#API Request - HTTP Request
import pytest
import requests

@pytest.mark.smoke
def test_get_single_request_by_id():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1")
    response_status = response.status_code
    print(response.json())
    print(response.cookies)
    print(response.headers)
    assert response_status == 200
