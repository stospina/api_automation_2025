import json
import logging
import os
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class ValidateResponse:
    def validate_response(self, actual_response,expected_response):
        #expected_response = self.read_input_data(f"src/api/input_json/{file_name}.json")

        self.validate_value(actual_response["body"], expected_response["expected_body"], "body")
        self.validate_value(
            actual_response["status_code"],
            expected_response["expected_status"],
            "status_code",
        )
        self.validate_value(
            actual_response["headers"], expected_response["headers"], "headers"
        )

    @staticmethod
    def validate_value(actual_value, expected_value, key_compare):
        if key_compare == "status_code":
            assert (
                actual_value == expected_value
            ), f"Expected status code: {expected_value} but received {actual_value}"
        elif key_compare == "headers":
            LOGGER.debug(f"Actual Headers: {actual_value}")
            LOGGER.debug(f"Expected Headers: {expected_value}")
            assert (
                expected_value.items() <= expected_value.items()
            ), f"Expected headers: {expected_value} but received {actual_value}"
        elif key_compare == "body":
            for k, v in expected_value.items():
                if k in actual_value:
                    assert actual_value[k] == v, f"Error '{k}': expected to be {v}, but it was {actual_value[k]}"


    def read_input_data(self,file_name):
        LOGGER.debug(f"Reading input data from {file_name}")
        if not os.path.exists(file_name):
             LOGGER.debug("Not file")

        with open(file_name, encoding="utf-8") as f:
            data = json.load(f)
        LOGGER.debug(f"Content data: {data}")
        return data
