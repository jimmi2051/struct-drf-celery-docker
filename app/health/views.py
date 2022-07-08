# Standard Library
import logging

# Third Party
import boto3
from infastructure.responses import FailedResponse
from infastructure.responses import SuccessResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .tasks import add

logger = logging.getLogger(__name__)


@api_view(['GET'])
def healthCheck(request):
    try:
        response_200 = {"description": "the service is healthy"}
        return SuccessResponse(response_200)

    except Exception as e:
        logger.error(str(e))
        return FailedResponse(
            status_message=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def testCelery(request):
    try:
        task = add.delay(2, 2)
        result = {"task_id": task.id, "status": "ok"}
        return SuccessResponse(result)
    except Exception as e:
        logger.error(str(e))
        return FailedResponse(status_message=str(e))


@api_view(['GET'])
def testS3Config(request):
    try:

        s3 = boto3.resource('s3')
        buckets = []
        for bucket in s3.buckets.all():
            buckets.append(bucket.name)
        result = {"status": "Ok", "buckets": buckets}
        return SuccessResponse(result)

    except Exception as e:
        logger.error(str(e))
        return FailedResponse(status_message=str(e))
