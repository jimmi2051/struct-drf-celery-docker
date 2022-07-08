# Third Party
from django.urls import include
from django.urls import path
from main.book.bookApi import BookAPI
from rest_framework.routers import DefaultRouter

main_router = DefaultRouter()
main_router.register(r'books', BookAPI, 'book-apis')

urlpatterns = [path('', include(main_router.urls))]
