def log_info(log, api_url, data):
    log.info('API [%s], [Data] %s' % (api_url, data))


def log_error(log, api_url, error):
    log.error('API [%s], [Error] %s' % (api_url, error))


def response_400():
    return {"description": "bad input parameter"}


def response_401():
    return {"description": "not authorized"}


def response_500():
    return {"description": "internal error"}
