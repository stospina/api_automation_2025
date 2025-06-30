import json
import logging
import random
import jsonschema
import pytest
from src.api.carbon_interface.schemas.electricity_estimate_schema import electricity_estimate_schema
from src.api.carbon_interface.schemas.flight_estimate_schema import flight_estimate_schema
from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
from config.config import url_base, headers
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

@pytest.mark.usefixtures("test_log_name")
class TestEstimates:

    @classmethod
    def setup_class(cls):
        """

        :return:
        """
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    def test_create_electricity(self):
        """
        Test for creating an electricity estimate
        :return:
        """
        units = ["kwh", "mwh"]

        payload = {
                "type": "electricity",
                "country": "us",
                "state": "fl",
                "electricity_unit": random.choice(units),
                "electricity_value": round(random.uniform(100, 1000), 2)
        }
        url_post_electricity =f"{url_base}estimates"

        response = self.rest_client.send_request(
            "POST",
            url=url_post_electricity,
            headers=headers,
            body=payload
        )

        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        try:
            jsonschema.validate(instance=response["body"], schema=electricity_estimate_schema)
            LOGGER.debug("Schema is valid")
        except jsonschema.exceptions.ValidationError as e:
            LOGGER.debug("JSON validator error: %s", e)
        assert response["status_code"] == 201


    def test_create_flight(self):
        """
        Test for creating a flight estimate
        :return:
        """

        payload = {
            "type": "flight",
            "passengers": 1,
            "legs": [
                {"departure_airport": "JFK", "destination_airport": "LAX"}
            ]
        }
        url_post_flight =f"{url_base}estimates"

        response = self.rest_client.send_request(
            "POST",
            url=url_post_flight,
            headers=headers,
            body=payload
        )

        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        try:
            jsonschema.validate(instance=response["body"], schema=flight_estimate_schema)
            LOGGER.debug("Schema is valid")
        except jsonschema.exceptions.ValidationError as e:
            LOGGER.debug("JSON validator error: %s", e)
        assert response["status_code"] == 201
