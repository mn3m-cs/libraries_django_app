from django.shortcuts import render
from .models import Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, FormView, DetailView
from rest_framework import generics
from users.models import UserProfile
from library.models import Book
from .serializers import ReviewSerializer


class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('title', 'body', 'rate', 'book', 'userProfile')
    template_name = 'library/books-media-detail-v2.html'


# REST Views
class AddReview(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        da = serializer.data
        user = self.request.user
        user_profile = UserProfile.objects.get(user=user)
        book_name = da['book_name']
        book = Book.objects.get(name=book_name)
        print(da, user_profile)
        # as a security check , but already we hide the review form from user.

        if Review.objects.filter(book=book, userProfile=user_profile).count() == 0:
            Review.objects.create(title=da['title'],
                                  body=da['body'],
                                  rate=da['rate'],
                                  book=book,
                                  userProfile=user_profile
                                  )
