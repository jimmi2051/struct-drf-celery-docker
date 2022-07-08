# Standard Library
import logging

# Third Party
from appcenter.configs.constants import MSG_CODE
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from djangorestframework_camel_case.util import camelize
from infastructure.responses import FailedResponse
from infastructure.responses import SuccessResponse
from rest_framework import status

logger = logging.getLogger("Render Response")


class JobhopCamelCaseJSONRenderer(CamelCaseJSONRenderer):
    def render(self, data, media_type, context, **kwargs):
        """wrap the data into a custom format
        If data has been wrapped already, do nothing
        """
        response = context.get('response')
        if isinstance(response, (SuccessResponse, FailedResponse)):
            return super().render(data, media_type, context, **kwargs)

        status_code = response.status_code
        success = status_code < status.HTTP_300_MULTIPLE_CHOICES
        status_message = "Success" if success else "Error"
        if not success:
            logger.info(f'render:{data}...')
            status_message = MSG_CODE[status_code]

            data = None
        data = camelize(data)

        data = {
            "success": success,
            "statusCode": status_code,
            "statusMessage": status_message,
            "data": data,
        }
        # Always return status 200
        context['response'].status_code = status.HTTP_200_OK
        return super().render(data, media_type, context, **kwargs)
