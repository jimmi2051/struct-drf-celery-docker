# Third Party
from entity.models import Book


class BookService:
    @classmethod
    def get_all(cls):
        return Book.objects.all()

    @classmethod
    def get_by_id(cls, id):
        return Book.objects.get(id=id)

    @classmethod
    def create(cls, data):
        return Book.objects.create(**data)

    @classmethod
    def update(cls, id, data):
        book = Book.objects.get(id=id)
        book.title = data['title']
        book.author = data['author']
        book.isbn = data['isbn']
        book.save()
        return book

    @classmethod
    def delete(cls, id):
        book = Book.objects.get(id=id)
        book.delete()
        return book
