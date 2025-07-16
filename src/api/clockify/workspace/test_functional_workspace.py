import logging
import json

import allure
import pytest

from config.config import url_clockify, headers_clockify
from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

@allure.story("Workspaces")
class TestEstimates:

    @classmethod
    def setup_class(cls):
        """

        :return:
        """
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    @pytest.mark.smoke
    def test_get_all_workspaces(self):
        """
        Get all the workspaces
        :return:
        """
        url_get_all_workspaces = f"{url_clockify}workspaces"

        response = self.rest_client.send_request(
            "GET",
            url=url_get_all_workspaces,
            headers=headers_clockify,
        )

        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))

        assert response["status_code"] == 200
