import logging

import allure
import jsonschema
import pytest
from faker.proxy import Faker

from src.api.clockify.schemas.tasks_post_schema import tasks_post_schema
from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
from utils.logger import get_logger
from config.config import url_clockify, headers_clockify, workspace_id

LOGGER = get_logger(__name__, logging.DEBUG)

@allure.story("End to End")
@allure.parent_suite("End to End")
@allure.label("Tester: Steven Ospina")
@allure.title("Create a Task: adding to a project")
@pytest.mark.usefixtures("test_log_name")
class TestE2e:

    @classmethod
    def setup_class(cls):
        """

        :return:
        """
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    @pytest.mark.E2E
    @allure.title("Test Create Task End to End")
    @allure.tag("E2E", "Acceptance")
    def test_e2e_tasks(self, create_project):
        """
        Create Task request
        :return:
        """
        payload = {
            "name": Faker().name(),
            "status": "DONE"
        }
        project = create_project
        url_post_task = f"{url_clockify}workspaces/{workspace_id}/projects/{project["id"]}/tasks"
        response = self.rest_client.send_request(
            "POST",
            url=url_post_task,
            headers=headers_clockify,
            body=payload
        )

        expected = {
            "headers": headers_clockify,
            "expected_body": payload,
            "expected_status": 201
        }

        self.validate.validate_response(response,expected)
        LOGGER.debug(response["body"])
        try:
            jsonschema.validate(instance=response["body"], schema=tasks_post_schema)
            LOGGER.debug("Schema is valid")
        except jsonschema.exceptions.ValidationError as e:
            LOGGER.debug("JSON validator error: %s", e)
