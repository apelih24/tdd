from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'owner', 'add_date')
        read_only_fields = ('id', 'add_date')
