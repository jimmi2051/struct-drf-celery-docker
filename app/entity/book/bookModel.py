# Third Party
from django.db import models
from infastructure.models import AuditMixin


class Book(AuditMixin):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        ordering = ['title']
