from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from src.utils.utils import Utils

import allure
import pytest


@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants().url_authentication(),
        auth=None,
        payload=payload_create_token(),
        in_json=False,
        headers=Utils().common_headers()
    )
    verify_http_status_code(response_data=response, expected_data=200)

    verify_json_token_not_null(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=APIConstants().url_create_booking(),
        auth=None,
        payload=payload_create_booking(),
        in_json=False,
        headers=Utils().common_headers()
    )
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_not_null(booking_id)
    return booking_id
