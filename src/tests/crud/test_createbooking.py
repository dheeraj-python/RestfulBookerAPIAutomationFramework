#here we will create single test case for Create Booking API

import allure
import pytest
#import json

from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verifications import *
from src.utils.utils import Utils


class TestCreateBookingAPI():

    @allure.title("Verify that new unique Booking should be created")
    def test_create_booking_positive(self):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            payload=payload_create_booking(),
            in_json=False,
            headers=Utils().common_headers()
        )
        verify_http_status_code(response_data=response, expected_data=200)
        verify_json_key_not_null(response.json()["bookingid"])

    @allure.title("Verify the negative test case")
    def test_create_booking_negative(self):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            payload={},
            in_json=False,
            headers=Utils().common_headers()
        )
        verify_http_status_code(response_data=response, expected_data=400)
