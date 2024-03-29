# Standard Library
import logging

# Config for message code
MSG_CODE = {
    200: "SUCCESS",
    202: "ACCEPTED",
    400: "BAD_REQUEST",
    401: "UNAUTHORIZED",
    403: "FORBIDDEN",
    404: "NOT_FOUND",
    405: "METHOD_NOT_ALLOWED",
    415: "CONTENT_TYPE_NOT_ALLOWED",
    500: "INTERNAL_SERVER",
}


EXAMPLE = 1
# Const for filters
INVALID_KEY = "INVALID_KEY"
INVALID_FORMAT = "INVALID_FORMAT"
TYPE_ATTRIBUTE = 'ATTRIBUTE'
TYPE_PROPERTY = 'PROPERTY'
INVALID_CONTENT = 'INVALID_CONTENT'
PAGE_SIZE = 10
logger_console = logging.getLogger(__name__)
