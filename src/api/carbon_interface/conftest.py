import json
import logging
import pytest

import requests

from config.config import headers, url_base, program_uuid
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

#Arrange
@pytest.fixture
def create_card_profile():
    LOGGER.info("create project fixture")
    # project body
    project_body = {
        "external_id": "12321311",
        "diet_habit": "omnivore",
        "transportation_method": "midsize_vehicle"
    }
    url_post_card_profiles = f"{url_base}carbon_ledger/programs/{program_uuid}/card_profiles"
    # call endpoint using requests
    response = requests.post(
        url=url_post_card_profiles, headers=headers, json=project_body
    )
    LOGGER.debug("Response: %s", response.json())

    # get id project
    card_id = response.json()["data"]["id"]
    # once the test ends yield call to delete the project
    return card_id


# Arrange
@pytest.fixture
def test_log_name(request):
    LOGGER.info(f"Start test '{request.node.name}'")

    def fin():
        LOGGER.info(f"End test '{request.node.name}'")

    request.addfinalizer(fin)
