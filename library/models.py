from django.db import models
from users.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User


# TODO convert library to account

class Libraryy(models.Model):
    #
    name = models.CharField(max_length=100, unique=True)
    lib_email = models.EmailField()
    established_at = models.DateField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("library:home")


class LibraryPhones(models.Model):
    library = models.ForeignKey(Libraryy, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    # class Meta:
    #     unique_together = [['library', 'phone']]

    def __str__(self):
        return self.phone


class LibraryAddresses(models.Model):
    library = models.ForeignKey(Libraryy, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address


class LibraryCities(models.Model):
    library = models.ForeignKey(Libraryy, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city


class LibraryCountries(models.Model):
    library = models.ForeignKey(Libraryy, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class Category(models.Model):
    title = models.CharField(max_length=30)
    dscription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

formats = (
    ('paper','Paper'),
    ('pdf','PDF'),
    ('epub','EPUB'),
)

class Book(models.Model):
    isbn = models.IntegerField(verbose_name="Book ISBN", unique=True)
    name = models.CharField(max_length=200)
    pub_date = models.DateField(verbose_name='Pulication Date')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    overall_rate = models.SmallIntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ], null=True, blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    # price = models.SmallIntegerField(null=True)
    cover = models.ImageField(upload_to='book_cover/', null=True, blank=True)
    description = models.TextField(null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.DO_NOTHING)
    edition = models.CharField(max_length=100)
    length = models.PositiveSmallIntegerField()
    book_format = models.CharField(choices=formats,max_length=10) #TODO: multiple select
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("library:home")  # kwargs={"pk": self.pk} TODO redirect to detail view


class AuthorBooks(models.Model):
    # TODO: in views beforeproccess tesi if user is_author
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author)


class LibraryBooks(models.Model):
    library = models.ForeignKey(Libraryy, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.SmallIntegerField(null=True, blank=True)
    amount = models.PositiveIntegerField(null=True)

    def __str__(self):
        book_library = str(self.book) + ' - '+  str(self.library) 
        return book_library


# TODO:

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


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    rate = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.name
