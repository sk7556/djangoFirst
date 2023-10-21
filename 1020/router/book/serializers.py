from rest_framework import seializers
from .models import Book

class BookSerializer(seializers.ModelSerializer):
    class Meta:
        model = Book
        