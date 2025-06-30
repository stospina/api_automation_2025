import json
import logging
import os

import requests

from config.config import url_base, headers, program_uuid
from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestEstimates:

    @classmethod
    def setup_class(cls):
        """

        :return:
        """
        cls.car_ids = []
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    def test_create_card_profile(self, test_log_name):

        payload = {
            "external_id": "12321311",
            "diet_habit": "omnivore",
            "transportation_method": "midsize_vehicle"
        }

        url_post_card_profiles = f"{url_base}carbon_ledger/programs/{program_uuid}/card_profiles"

        response = self.rest_client.send_request(
            "POST",
            url=url_post_card_profiles,
            headers=headers,
            body=payload
        )
        card_id = response["body"]["data"]["id"]
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        self.car_ids.append(card_id)
        LOGGER.debug("Response: %s", json.dumps(response["body"]["data"], indent=4))


        assert response["status_code"] == 201

    def test_get_cards_profile(self, test_log_name, create_card_profile):
        card_id = create_card_profile
        url_get_card_profiles = f"{url_base}carbon_ledger/programs/{program_uuid}/card_profiles"

        response = self.rest_client.send_request(
            "GET",
            url=url_get_card_profiles,
            headers=headers,
        )

        self.car_ids.append(card_id)
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))

        assert response["status_code"] == 200

    def test_get_card_id_profile(self, create_card_profile):
        card_id = create_card_profile
        url_get_card_profiles = f"{url_base}carbon_ledger/programs/{program_uuid}/card_profiles"

        response = self.rest_client.send_request(
            "GET",
            url=url_get_card_profiles,
            headers=headers,
        )
        self.car_ids.append(card_id)
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))

        assert response["status_code"] == 200

    def test_update_card_profile(self, test_log_name,create_card_profile):
        card_id = create_card_profile
        payload = {
            "transportation_method": "midsize_vehicle"
        }

        url_patch_card_profiles = f"{url_base}carbon_ledger/programs/{program_uuid}/card_profiles/{card_id}"

        response = self.rest_client.send_request(
            "PATCH",
            url=url_patch_card_profiles,
            headers=headers,
            body=payload
        )
        card_id = response["body"]["data"]["id"]
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        self.car_ids.append(card_id)
        LOGGER.debug("Response: %s", json.dumps(response["body"]["data"], indent=4))

        assert response["status_code"] == 200

    def test_delete_cards_profile(self, test_log_name, create_card_profile):
        card_id = create_card_profile
        url_delete_card_profiles = f"{url_base}carbon_ledger/programs/{program_uuid}/card_profiles/{create_card_profile}"

        response = self.rest_client.send_request(
            "DELETE",
            url=url_delete_card_profiles,
            headers=headers,
        )
        self.car_ids.append(card_id)
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        assert response["status_code"] == 204

    def test_negative_create_card_profile(self, test_log_name):

        payload = {
            "external_id": "12321311",
            "diet_habit": "omnivore",
            "transportation_method": 1
        }

        url_post_card_profiles = f"{url_base}carbon_ledger/programs/{program_uuid}/card_profiles"

        response = self.rest_client.send_request(
            "POST",
            url=url_post_card_profiles,
            headers=headers,
            body=payload
        )
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        name = "negative_create_card"
        base_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(base_dir)
        file_path = os.path.join(parent_dir, f"input_json", f"{name}.json")
        LOGGER.debug(file_path)
        expected_response = self.validate.read_input_data(file_path)
        self.validate.validate_response(response,expected_response)
        assert response["status_code"] == 422

    @classmethod
    def teardown_class(cls):
        """
        Clean up after all tests
        :return:
        """
        # Cleanup projects
        LOGGER.info("Test teardown Class")
        for card_id in cls.car_ids:
            url_delete_card_profiles = f"{url_base}carbon_ledger/programs/{program_uuid}/card_profiles/{card_id}"
            LOGGER.debug(f"URL delete project: {url_delete_card_profiles}")
            response = requests.delete(
                url=url_delete_card_profiles,
                headers=headers,
            )

            LOGGER.debug("Status Code: %s", str(response.status_code))
            if response.status_code == 204:
                LOGGER.debug("Project deleted")
