# Standard Library
import logging

# Third Party
from appcenter.configs.constants import INVALID_CONTENT
from appcenter.configs.constants import MSG_CODE
from django.http.response import Http404
from infastructure.responses import FailedResponse
from rest_framework import exceptions
from rest_framework import status

logger = logging.getLogger("Exception Handler")


class StringValidationError:
    def __init__(self, detail):

        if hasattr(detail, "detail"):
            detail = detail.detail
        self.detail = detail

    def __str__(self):
        if isinstance(self.detail, list):
            errors = [err[0] for err in self.detail if isinstance(err, list)]
            errors.extend([err for err in self.detail if isinstance(err, str)])

            error = ", ".join(errors)
        elif isinstance(self.detail, dict):
            errors = []
            for k, v in self.detail.items():
                err = list(v)[0]
                value = f'{err}'
                # use value only for translation
                if 'non_field' in k:
                    value = f'{err}'
                errors.append(value)

                break

            error = ", ".join(errors)
        else:
            error = str(self.detail)
        return error


def custom_exception_handler(exc, context):
    logger.info(f'[ERROR] Exception > {exc} > type {type(exc)}')

    if isinstance(exc, exceptions.AuthenticationFailed) or isinstance(
        exc, exceptions.NotAuthenticated
    ):
        return FailedResponse(
            status=status.HTTP_401_UNAUTHORIZED,
            status_code=status.HTTP_401_UNAUTHORIZED,
            status_message=MSG_CODE[status.HTTP_401_UNAUTHORIZED],
        )

    if isinstance(exc, exceptions.PermissionDenied):

        return FailedResponse(
            status=status.HTTP_200_OK,
            status_code=status.HTTP_403_FORBIDDEN,
            status_message=MSG_CODE[status.HTTP_403_FORBIDDEN],
        )

    if isinstance(exc, exceptions.NotFound):
        error = StringValidationError(exc.detail).__str__()
        return FailedResponse(
            data=None, status_code=status.HTTP_404_NOT_FOUND, status_message=error
        )

    if isinstance(exc, Http404):
        return FailedResponse(
            data=None, status_code=status.HTTP_404_NOT_FOUND, status_message=str(exc)
        )

    if isinstance(exc, (exceptions.ValidationError, exceptions.APIException)):
        error = StringValidationError(exc.detail).__str__()

        return FailedResponse(
            data=None, status_code=status.HTTP_400_BAD_REQUEST, status_message=error
        )

    if isinstance(exc, (UnicodeDecodeError, AttributeError)):
        return FailedResponse(
            data=None,
            status_code=status.HTTP_400_BAD_REQUEST,
            status_message=INVALID_CONTENT,
        )

    if isinstance(exc, Exception):
        return FailedResponse(
            data=None,
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            status_message=str(exc),
        )

    logger.error(f'[ERROR] Cannot handle this error > {exc} > type {type(exc)}')

    return FailedResponse(
        data=None,
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        status_message=MSG_CODE[status.HTTP_500_INTERNAL_SERVER_ERROR],
    )
