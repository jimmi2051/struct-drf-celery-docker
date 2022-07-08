# Third Party
from django.contrib import admin
from entity.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
