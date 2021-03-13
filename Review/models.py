from django.db import models
from library.models import Book
from users.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    rate = models.SmallIntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
