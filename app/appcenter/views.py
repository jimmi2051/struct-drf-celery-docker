from sentry_sdk import capture_message
from django.http import JsonResponse
from rest_framework import status


def page_not_found(*args, **kwargs):
    capture_message("Page not found!", level="error")
    final_result = {
        "message": "Not found !"
    }
    # return any response here, e.g.:
    return JsonResponse(data=final_result, safe=False, status=status.HTTP_404_NOT_FOUND)
