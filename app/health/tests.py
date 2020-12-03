import json
from django.test import SimpleTestCase
from django.test.client import RequestFactory
from health.views import healthCheck


class ViewsTest(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()
    # Create your tests here.

    def test_healthCheck(self):
        request = self.factory.get("/auth/healthCheck")
        response = healthCheck(request)
        response_content = json.loads(response.content)
        expect_response = {
            "description": "the service is healthy"
        }
        self.assertEqual(expect_response, response_content)
