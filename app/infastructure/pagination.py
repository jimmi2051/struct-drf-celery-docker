# Third Party
from appcenter.configs.constants import PAGE_SIZE
from django.core.paginator import InvalidPage
from infastructure.responses import PaginationResponse
from rest_framework import pagination
from rest_framework.exceptions import NotFound


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'pageSize'

    def get_page_size(self, request):
        ps = super().get_page_size(request)
        if not ps:
            ps = PAGE_SIZE
        return ps

    def get_paginated_response(self, data):
        return PaginationResponse(
            data,
            total=self.page.paginator.count,
            next_link=self.get_next_link(),
            previous_link=self.get_previous_link(),
            current_page=self.page.number,
            page_size=self.get_page_size(self.request),
            page_count=self.page.paginator.num_pages,
        ).response

    def get_page_number(self, request, paginator):
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'total': {'type': 'integer', 'example': 123},
                'next': {'type': 'string', 'nullable': True},
                'previous': {'type': 'string', 'nullable': True},
                'collections': schema,
                'page': {'type': 'int', 'nullable': True},
                'pageSize': {'type': 'int', 'nullable': True},
                'pageCount': {'type': 'int', 'nullable': True},
            },
        }

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)

        try:
            if int(page_number) > int(paginator.num_pages):
                page_number = 1
            self.page = paginator.page(page_number)
        except (InvalidPage, ValueError) as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=str(exc)
            )
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)
