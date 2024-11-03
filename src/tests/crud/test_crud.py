#here we will perform CRUD operation on APIwhere we will
#create token
#create booking ID
#Update Booking ID
#delete booking

from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from src.utils.utils import Utils

import allure
import pytest
import json


class TestCrud(object):

    @allure.title("Test CRUD Operation")
    def test_update_booking_id(self, create_token, get_booking_id):

        put_url = APIConstants.url_patch_put_del(booking_id=get_booking_id)

        response = put_request(
            url=put_url,
            headers=Utils().common_headers_put_patch_delete_cookie(token=create_token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_key(response.json()["firstname"], "Neha")
        verify_response_key(response.json()["totalprice"], expected_data=101)
