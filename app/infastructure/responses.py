# Third Party
from appcenter.configs.constants import PAGE_SIZE
from rest_framework import status
from rest_framework.response import Response


class PaginationResponse:
    current_page = 1

    def __init__(
        self,
        data,
        total=0,
        current_page=1,
        page_count=1,
        page_size=None,
        next_link=None,
        previous_link=None,
    ):
        self._data = data
        self.total = total
        self.next_link = next_link
        self.previous_link = previous_link
        self.page_count = page_count
        if current_page:
            self.current_page = current_page
        if page_size:
            self.page_size = page_size
        else:
            self.page_size = PAGE_SIZE

    @property
    def response(self):
        return SuccessResponse(
            {
                'links': {'next': self.next_link, 'previous': self.previous_link},
                'total': self.total,
                'collections': self._data,
                'page': self.current_page,
                'page_size': self.page_size,
                'page_count': self.page_count,
            }
        )


class FailedResponse(Response):
    response_data = {
        "success": False,
        "statusCode": 400,
        "statusMessage": "",
        "data": None,
    }

    def __init__(self, data=None, status_code=400, status_message='', **kwargs):
        response_data = self.response_data
        response_data['statusMessage'] = status_message
        response_data['statusCode'] = status_code
        response_data['data'] = data
        data = response_data
        super().__init__(data, **kwargs)


class SuccessResponse(Response):
    response_data = {
        "success": True,
        "statusCode": 0,
        "statusMessage": "Success",
        "data": None,
    }

    def __init__(self, data=None, status_code=200, status_message='Success', **kwargs):
        response_data = self.response_data
        response_data['statusMessage'] = status_message
        response_data['statusCode'] = status_code
        response_data['data'] = data
        data = response_data
        super().__init__(data, **kwargs)


class RawResponse(Response):
    def __init__(self, data=None, **kwargs):
        super().__init__(data, **kwargs)


def is_success_response(response):
    if response.status_code == status.HTTP_200_OK and isinstance(
        response, SuccessResponse
    ):
        return True
    return False
