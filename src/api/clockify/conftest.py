import logging
import pytest

import requests

from src.api.clockify.payloads.projects_payloads import project_payload
from src.api.clockify.payloads.clients_payloads import clients_post_payload
from config.config import url_clockify, headers_clockify, workspace_id
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

#Arrange

@pytest.fixture
def create_project(project_payload):
    """
    Hook to create a project
    :return:
    """

    LOGGER.info("create project fixture")
    # project body
    project_body = project_payload
    url_post_projects = f"{url_clockify}workspaces/{workspace_id}/projects/"
    # call endpoint using requests
    response = requests.post(
        url=url_post_projects, headers=headers_clockify, json=project_body
    )
    LOGGER.debug("Response: %s", response.json())

    # get id project
    project_id = response.json()["id"]
    # once the test ends yield call to delete the project
    yield {
        "id": project_id,
        "body": response.json(),
        "status_code": response.status_code,
        "headers": response.headers,
        "expected_body": project_body,
        "expected_status": 201
    }
    clean_project(project_id)

def clean_client(client_id):
    """
            Clean up after all tests
            :return:
            """
    # Cleanup projects
    LOGGER.info("Test teardown Class")
    url_delete_clients_by_id = f"{url_clockify}workspaces/{workspace_id}/clients/{client_id}"
    LOGGER.debug(f"URL delete project: {url_delete_clients_by_id}")
    response_archived = requests.put(url=url_delete_clients_by_id, headers=headers_clockify, json={"archived": True})
    LOGGER.debug("Status Code: %s", str(response_archived.status_code))
    response = requests.delete(
        url=url_delete_clients_by_id,
        headers=headers_clockify,
    )

    LOGGER.debug("Status Code: %s", str(response.status_code))
    if response.status_code == 200:
        LOGGER.debug("Project deleted")

@pytest.fixture
def create_client(clients_post_payload):
    """
    Hook to create a client
    :return:
    """

    LOGGER.info("create client fixture")
    # project body
    client_body = clients_post_payload
    url_post_projects = f"{url_clockify}workspaces/{workspace_id}/clients"
    # call endpoint using requests
    response = requests.post(
        url=url_post_projects, headers=headers_clockify, json=client_body
    )
    LOGGER.debug("Response: %s", response.json())

    # get id project
    client_id = response.json()["id"]
    # once the test ends yield call to delete the project
    yield {
        "id": client_id,
        "body": response.json(),
        "status_code": response.status_code,
        "headers": response.headers,
        "expected_body": client_body,
        "expected_status": 201
    }
    clean_client(client_id)




# Arrange
@pytest.fixture
def test_log_name(request):
    LOGGER.info(f"Start test '{request.node.name}'")

    def fin():
        LOGGER.info(f"End test '{request.node.name}'")

    request.addfinalizer(fin)


def clean_project(project_id):
        """
        Clean up after all tests
        :return:
        """
        # Cleanup projects
        LOGGER.info("Test teardown Class")
        url_delete_workspace_by_id = f"{url_clockify}workspaces/{workspace_id}/projects/{project_id}"
        LOGGER.debug(f"URL delete project: {url_delete_workspace_by_id}")
        response_archived = requests.put(url=url_delete_workspace_by_id,headers=headers_clockify,json={"archived":True})
        LOGGER.debug("Status Code: %s", str(response_archived.status_code))
        response = requests.delete(
            url=url_delete_workspace_by_id,
            headers=headers_clockify,
        )

        LOGGER.debug("Status Code: %s", str(response.status_code))
        if response.status_code == 200:
            LOGGER.debug("Project deleted")
