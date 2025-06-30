import pytest
from faker import Faker

@pytest.fixture
def project_payload():
    """
    POST payload
    :return: dictionary with the body
    """
    return {
        "name": f"{Faker().company()}",
        "billable": True,
        "isPublic": True
    }

@pytest.fixture
def project_put_payload():
    """
    POST payload
    :return: dictionary with the body
    """
    return {
        "archived": False,
        "name": f"{Faker().company()}",
        "billable": True,
        "isPublic": True,
        "note": f"{Faker().sentence(3)}"
    }
