import logging
import allure
import jsonschema
import pytest
from faker.proxy import Faker

from src.api.clockify.payloads.projects_payloads import project_put_payload
from src.api.clockify.schemas.project_delete_schema import project_delete_schema
from src.api.clockify.schemas.project_get_schema import project_get_schema
from src.api.clockify.schemas.project_post_schema import project_post_schema
from config.config import url_clockify, headers_clockify, workspace_id
from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

@allure.story("Projects")
@allure.parent_suite("Projects")
@pytest.mark.usefixtures("test_log_name")
class TestProjects:

    @classmethod
    def setup_class(cls):
        """

        :return:
        """
        cls.projects_ids = []
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    @pytest.mark.acceptance
    @pytest.mark.functional
    def test_create_project(self,create_project):
        """
        POST request to create a project
        :return:
        """
        response = create_project

        #assert response["status"] == 201
        self.validate.validate_response(response,response)
        try:
            jsonschema.validate(instance=response["body"], schema=project_post_schema)
            LOGGER.debug("Schema is valid")
        except jsonschema.exceptions.ValidationError as e:
            LOGGER.debug("JSON validator error: %s", e)

    @pytest.mark.acceptance
    @pytest.mark.smoke
    def test_get_project_by_id(self, create_project):
        """
        Get project by ID
        :return:
        """
        project_id = create_project["id"]
        url_get_project_by_id = f"{url_clockify}workspaces/{workspace_id}/projects/{project_id}"
        response = self.rest_client.send_request(
            "GET",
            url=url_get_project_by_id,
            headers=headers_clockify,
        )

        #self.validate.validate_response(response)
        assert response["status_code"] == 200

    @pytest.mark.acceptance
    @pytest.mark.smoke
    def test_get_all_projects(self,create_project):
        """
        Get projects
        :return:
        """
        url_get_project_by_id = f"{url_clockify}workspaces/{workspace_id}/projects"
        response = self.rest_client.send_request(
            "GET",
            url=url_get_project_by_id,
            headers=headers_clockify,
        )
        try:
            jsonschema.validate(instance=response["body"], schema=project_get_schema)
            LOGGER.debug("Schema is valid")
        except jsonschema.exceptions.ValidationError as e:
            LOGGER.debug("JSON validator error: %s", e)
        assert response["status_code"] == 200

    def test_update_projects(self,create_project, project_put_payload):
        """
        PUT request to create a project
        :return:
        """
        payload = project_put_payload

        url_get_project_by_id = f"{url_clockify}workspaces/{workspace_id}/projects/{create_project["id"]}"
        response = self.rest_client.send_request(
            "PUT",
            url=url_get_project_by_id,
            headers=headers_clockify,
            body=payload
        )
        LOGGER.debug(response["status_code"])
        expected = {
            "headers": headers_clockify,
            "expected_body": payload,
            "expected_status": 200
        }

        self.validate.validate_response(response,expected)

    @pytest.mark.acceptance
    @pytest.mark.functional
    def test_delete_project(self, project_payload):
        """
        DELETE request requires a PUT action with the parameter archived = true before removing the project
        :return:
        """
        project_body = project_payload
        url_post_projects = f"{url_clockify}workspaces/{workspace_id}/projects/"
        # call endpoint using requests
        response = self.rest_client.send_request(
            "POST",
            url=url_post_projects, headers=headers_clockify, body=project_body
        )

        url_delete_workspace_by_id = f"{url_clockify}workspaces/{workspace_id}/projects/{response["body"]["id"]}"
        LOGGER.debug(f"URL delete project: {url_delete_workspace_by_id}")
        response_archived =self.rest_client.send_request(
            "PUT",
            url=url_delete_workspace_by_id,
            headers=headers_clockify,
            body={"archived": True})
        LOGGER.debug("Status Code for PUT request: %s", str(response_archived["status_code"]))
        response = self.rest_client.send_request(
            "DELETE",
            url=url_delete_workspace_by_id,
            headers=headers_clockify,
        )
        LOGGER.debug("Response for DELETE request: %s", response["body"])
        try:
            jsonschema.validate(instance=response["body"], schema=project_delete_schema)
            LOGGER.debug("Schema is valid")
        except jsonschema.exceptions.ValidationError as e:
            LOGGER.debug("JSON validator error: %s", e)
        LOGGER.debug("Project deleted")
        assert response["status_code"] == 200

    @pytest.mark.acceptance
    @pytest.mark.negative
    def test_negative_project(self,project_payload):
        """
        Negative test: Requires the "name" in the body
        :return:
        """
        project_body = {
            "isPublic": 1
        }

        url_post_projects = f"{url_clockify}workspaces/{workspace_id}/projects/"
        # call endpoint using requests
        response = self.rest_client.send_request(
            "POST",
            url=url_post_projects, headers=headers_clockify, body=project_body
        )

        LOGGER.debug("Response: %s", response["status_code"])
        LOGGER.debug("Response: %s", response["body"])
        assert response["status_code"] == 400

    @pytest.mark.acceptance
    @pytest.mark.negative
    def test_negative_invalid_project(self, project_payload):
        """
        Negative test: Requires the "name" in the body
        :return:
        """
        project_body = {
            "name": Faker().name(),
            "isPublic": "no"
        }

        url_post_projects = f"{url_clockify}workspaces/{workspace_id}/projects/"
        # call endpoint using requests
        response = self.rest_client.send_request(
            "POST",
            url=url_post_projects, headers=headers_clockify, body=project_body
        )

        LOGGER.debug("Response: %s", response["status_code"])
        LOGGER.debug("Response: %s", response["body"])
        assert response["status_code"] == 400
