from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions
from users.models import UserProfile
from .models import Libraryy,LibraryBooks,Book
from .serializer import LibrarySerializer,LibraryBooksSerializer

from rest_framework.generics import get_object_or_404

class Libraries(generics.ListAPIView):
    """
    libraries search on add_book
    """
    queryset = Libraryy.objects.all()
    serializer_class = LibrarySerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name']

class IsUserIsAuthor(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        userprofile = UserProfile.objects.get(user=request.user)
        return userprofile.is_author

class AddLibraryBookAPIView(generics.CreateAPIView):
    serializer_class = LibraryBooksSerializer
    queryset = LibraryBooks.objects.all()
    permission_classes = [IsUserIsAuthor]

    def perform_create(self, serializer):
        da = serializer.data
        book_isbn = da['book_isbn']
        lib_name = da['lib_name']
        #TODO: book is not created yet, we need to create it here first
        book = Book.objects.get(isbn=book_isbn)
        libra = Libraryy.objects.get(name=lib_name)
        LibraryBooks.objects.create(library=libra,book=book)

        # if serializer.is_valid():
        #     serializer.validated_data['library'] = libra
        #     serializer.validated_data['book'] = book
        #     print(serializer.validated_data)

            # return LibraryBooks(**serializer.validated_data)
            # serializer.save()


        #         book = Book.objects.get(isbn=book_isbn)
        # libra = Libraryy.objects.get(name=lib_name)
        # print(lib_name,book)
        # we get names , >>> use models to get pk and then save them
