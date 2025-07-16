import logging

from faker import Faker
from config.config import url_clockify, headers_clockify, workspace_id
from helper.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


def before_all(context):
    """
     Setup before all Features.
    :param context:  Object  stores test data
    """

    LOGGER.debug("Before all tests")
    context.headers = headers_clockify
    context.url_clockify = url_clockify
    context.workspace_id= workspace_id
    context.rest_client = RestClient()
    context.project_list = []


def before_feature(context, feature):
    """
    Setup before feature.
    :param context:
    :param feature:
    :return:
    """
    LOGGER.debug("Before feature")


def client_payload():
    return {
        "address": f"{Faker().address()}",
        "email": f"{Faker().email()}",
        "name": f"{Faker().name()}",
        "note": f"{Faker().sentence(4)}"
    }


def before_scenario(context, scenario):
    if "project_id" in scenario.tags:
        LOGGER.info("create project fixture")
        # project body
        project_body = project_payload()
        LOGGER.debug("Project payload: %s", project_body)
        url_post_projects = f"{context.url_clockify}workspaces/{context.workspace_id}/projects/"
        # call endpoint using requests
        response = context.rest_client.send_request(
            "POST",
            url=url_post_projects, headers=headers_clockify, body=project_body
        )

        # get id project
        context.project_id = response["body"]["id"]
        #context.project_list.append(context.project_id)
        LOGGER.debug("Project ID: %s", response["body"]["id"])
    if "client_id" in scenario.tags:
        LOGGER.info("create client fixture")
        client_body = client_payload()
        url_post_clients = f"{url_clockify}workspaces/{workspace_id}/clients"
        # call endpoint using requests
        response = context.rest_client.send_request(
            "POST",
            url=url_post_clients, headers=headers_clockify, body=client_body
        )
        # get id client
        context.client_id = response["body"]["id"]
        # context.project_list.append(context.project_id)
        LOGGER.debug("Project ID: %s", response["body"]["id"])


def project_payload():
    return {
        "name": f"{Faker().company()}",
        "billable": True,
        "isPublic": True
    }

def after_scenario(context, scenario):
    """
    Tear down after the scenario.
    :param context:
    :param scenario:
    :return:
    """
    LOGGER.debug('Ending scenario: "%s"', scenario.name)
    if "clean" in scenario.tags:
        #for project_id in context.project_list:
        if hasattr(context, "project_id") or "Projects" in scenario.tags:
            url_delete_entity = f"{context.url_clockify}workspaces/{context.workspace_id}/projects/{context.project_id}"
            context.entity_id = context.project_id
        # elif hasattr(context, "task_id"):
        #     url_delete_entity = f"{context.url_clockify}workspaces/{context.workspace_id}/projects/{context.project_id}/tasks/{context.task_id}"
        #     context.entity_id = context.task_id

        if hasattr(context, "client_id") or "Clients" in scenario.tags:
            url_delete_entity = f"{context.url_clockify}workspaces/{context.workspace_id}/clients/{context.client_id}"
            context.entity_id = context.client_id

        response_archived = context.rest_client.send_request(
            "PUT", url=url_delete_entity, headers=context.headers, body={"archived":True}
        )

        response = context.rest_client.send_request(
            "DELETE", url=url_delete_entity, headers=context.headers
        )
        if response["status_code"] == 200:
            LOGGER.debug("Entity %s deleted", context.entity_id)

