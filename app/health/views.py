import logging
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from appcenter.utils import response_500, log_error
from .tasks import add
logger = logging.getLogger(__name__)


@api_view(['GET'])
def healthCheck(request):
    try:
        response_200 = {"description": "the service is healthy"}

        return JsonResponse(data=response_200,
                            safe=False,
                            status=status.HTTP_200_OK)

    except Exception as e:
        log_error(logger, "healthCheck", str(e))
        return JsonResponse(data=response_500(),
                            safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def testCelery(request):
    try:
        task = add.delay(2, 2)
        result = {"task_id": task.id, "status": "ok"}
        return JsonResponse(data=result, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        log_error(logger, "celeryConfig", str(e))
        return JsonResponse(data=response_500(),
                            safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def testS3Config(request):
    try:
        import boto3
        s3 = boto3.resource('s3')
        buckets = []
        for bucket in s3.buckets.all():
            buckets.append(bucket.name)
        result = {"status": "Ok", "buckets": buckets}
        return JsonResponse(data=result, safe=False, status=status.HTTP_200_OK)

    except Exception as e:
        log_error(logger, "S3Config", str(e))
        return JsonResponse(data=response_500(),
                            safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
