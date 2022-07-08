# Standard Library
import logging

# Third Party
from django.test import TestCase

from .views import page_not_found

logger = logging.getLogger("logger_test")


class ViewsTest(TestCase):
    def tests_page_not_found(self):
        expect_response = {"message": "Not found !"}
        response = page_not_found()
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(str(response.content, encoding='utf8'), expect_response)
