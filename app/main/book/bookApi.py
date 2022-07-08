# Third Party
from infastructure.filters import process_filter_and_search
from infastructure.pagination import CustomPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from service.book.bookSerializers import BookSerializer
from service.book.bookService import BookService


# Create your views here.
class BookAPI(ModelViewSet):
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'post']
    ALLOW_FIELDS_FILTER = {"isbn": "isbn"}
    ALLOW_FIELDS_SEARCH = ["title__icontains", "author__icontains"]
    ALLOW_FIELDS_SORT = {
        "createdAt:asc": "created_at",
        "createdAt:desc": "-created_at",
        "updatedAt:asc": "updated_at",
        "updatedAt:desc": "-updated_at",
    }

    def get_queryset(self):
        return BookService.get_all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = process_filter_and_search(
            request,
            self.ALLOW_FIELDS_SORT,
            self.ALLOW_FIELDS_FILTER,
            self.ALLOW_FIELDS_SEARCH,
            queryset,
        )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
