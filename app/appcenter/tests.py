from django.test import TestCase
import requests
import json
import logging
from mock import Mock, patch
from .views import page_not_found
from .utils import log_info, log_error, response_400, response_401, response_500

logger = logging.getLogger("logger_test")


class ViewsTest(TestCase):
    def tests_page_not_found(self):
        expect_response = {"message": "Not found !"}
        response = page_not_found()
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
                             expect_response)


class UtilsTest(TestCase):
    def tests_log_info(self):
        with self.assertLogs(logger="logger_test", level="INFO") as cm:
            log_info(logger, "/healthCheck", "Ok")
            self.assertIn("INFO:logger_test:API [/healthCheck], [Data] Ok",
                          cm.output)

    def tests_log_error(self):
        with self.assertLogs(logger="logger_test", level="ERROR") as cm:
            log_error(logger, "/healthCheck", "Internal Server")
            self.assertIn(
                "ERROR:logger_test:API [/healthCheck], [Error] Internal Server",
                cm.output)

    def tests_response_400(self):
        expect_response = {"description": "bad input parameter"}
        response = response_400()
        self.assertEqual(expect_response, response)

    def tests_response_401(self):
        expect_response = {"description": "not authorized"}
        response = response_401()
        self.assertEqual(expect_response, response)

    def tests_response_500(self):
        expect_response = {"description": "internal error"}
        response = response_500()
        self.assertEqual(expect_response, response)
