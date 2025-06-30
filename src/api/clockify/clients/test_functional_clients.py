import logging

import allure
import jsonschema
import pytest
from src.api.clockify.schemas.clients_post_schema import clients_post_schema
from config.config import url_clockify, headers_clockify, workspace_id
from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

@allure.story("Clients")
@allure.parent_suite("Clients")
@pytest.mark.usefixtures("test_log_name")
class TestClients:

    @classmethod
    def setup_class(cls):
        """

        :return:
        """
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    @pytest.mark.acceptance
    @pytest.mark.functional
    def test_create_clients(self, create_client):
        """
        POST request to create a client
        :return:
        """
        response = create_client

        self.validate.validate_response(response,response)
        try:
            jsonschema.validate(instance=response["body"], schema=clients_post_schema)
            LOGGER.debug("Schema is valid")
        except jsonschema.exceptions.ValidationError as e:
            LOGGER.debug("JSON validator error: %s", e)

    @pytest.mark.acceptance
    @pytest.mark.functional
    def test_get_clients(self, create_client):
        """
        GET request to retrieve all clients
        :return:
        """

        url_get_project_by_id = f"{url_clockify}workspaces/{workspace_id}/clients"
        response = self.rest_client.send_request(
            "GET",
            url=url_get_project_by_id,
            headers=headers_clockify,
        )

        try:
            jsonschema.validate(instance=response["body"], schema=clients_post_schema)
            LOGGER.debug("Schema is valid")
        except jsonschema.exceptions.ValidationError as e:
            LOGGER.debug("JSON validator error: %s", e)

        assert response["status_code"] == 200


