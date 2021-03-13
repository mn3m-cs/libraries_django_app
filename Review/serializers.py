from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='book.name')

    class Meta:
        model = Review
        fields = ('title', 'body', 'rate', 'book_name',)
