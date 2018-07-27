from django_elasticsearch_dsl import DocType, Index
from api.models import Book

books = Index('books')


@books.doc_type
class BookDocument(DocType):
    class Meta:
        model = Book

        fields = [
            'name',
            'author',
            'add_date',
            'id'
        ]
