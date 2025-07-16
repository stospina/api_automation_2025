import logging

from behave import then

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

@then("the status code is {status_code:d}")
def verify_status_code(context, status_code):
    LOGGER.debug("Step verify status code %s", status_code)
    assert context.status_code == status_code