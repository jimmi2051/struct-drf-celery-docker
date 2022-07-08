# Third Party
from entity.models import Book
from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'title': {'required': True},
            'author': {'required': True},
            'isbn': {'required': True},
        }
