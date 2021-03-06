from rest_framework import serializers
from .models import Libraryy,Book,LibraryBooks

class LibrarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Libraryy
        fields = ['name',]

# class BookSerializer(serializers.ModelSerializer):
#     # bpk= serializers.CharField(source='pk')
#     class Meta:
#         model = Book
#         fields = ['isbn']
        
class LibraryBooksSerializer(serializers.ModelSerializer):
    lib_name = serializers.CharField(source='library.name')
    book_isbn = serializers.CharField(source='book.isbn')
    
    class Meta:
        model = LibraryBooks
        fields = ['lib_name','book_isbn']
