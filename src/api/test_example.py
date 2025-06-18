import logging
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestExample:

    @classmethod
    def setup_class(cls):
        """
        Setup class
        :return:
        """
        API_KEY = "3Zo9k91XvEs4XgF97Ulwg"
        LOGGER.info('Setup class')
        cls.header_api = {
            "Authorization": "Bearer {}".format(API_KEY)
        }
        LOGGER.debug("Header API: %s", cls.header_api)

    def test_one(self):
        LOGGER.info('Test one')
        #assert


    def test_two(self):
        LOGGER.info('Test two')

    def test_three(self):
        LOGGER.info('Test three')

    @classmethod
    def teardown_class(cls):
        LOGGER.info('Teardown class')
