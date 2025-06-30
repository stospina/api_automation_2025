import pytest
from faker import Faker

@pytest.fixture
def clients_post_payload():
    """
    POST payload for clients
    :return: dictionary with the body
    """
    return {

        "address": f"{Faker().address()}",
        "email": f"{Faker().email()}",
        "name": f"{Faker().name()}",
        "note": f"{Faker().sentence(4)}"

    }