from django.db import models
from users.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Libraryy(models.Model):
    name = models.CharField(max_length=100,unique=True)
    lib_email = models.EmailField()
    established_at = models.DateField()
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("library:home")
    
    # def save(self):

class LibraryPhones(models.Model):
    library = models.ForeignKey(Libraryy,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    
    # class Meta:
    #     unique_together = [['library', 'phone']]

    def __str__(self):
        return self.phone

class LibraryAddresses(models.Model):
    library = models.ForeignKey(Libraryy,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address    

class LibraryCities(models.Model):
    library = models.ForeignKey(Libraryy,on_delete=models.CASCADE)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city

class LibraryCountries(models.Model):
    library = models.ForeignKey(Libraryy,on_delete=models.CASCADE)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country

class Category(models.Model):
    title = models.CharField(max_length=30)
    dscription = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    isbn = models.IntegerField(verbose_name="Book ISBN",unique=True)
    name = models.CharField(max_length=200)
    pub_date = models.DateField(verbose_name='Pulication Date')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    overall_rate = models.SmallIntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],null=True,blank=True)
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE,blank=True,null=True)
    price = models.SmallIntegerField()
    cover = models.ImageField(upload_to='book_cover/',null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("library:home") #kwargs={"pk": self.pk}

class AuthorBooks(models.Model):
    # TODO: in views beforeproccess tesi if user is_author
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author)

#TODO:
class LibraryBooks(models.Model):
    library = models.ForeignKey(Libraryy,on_delete=models.CASCADE)
    book =models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book)

class Review(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    rate = models.SmallIntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    UserProfile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class CreditCard(models.Model):
    card_number = models.CharField(max_length=14,unique=True)
    expxire_date = models.DateField()
    # card_type = models.

    def __str__(self):
        return self.card_number

class UserCards(models.Model):
    credit_card = models.ForeignKey(CreditCard,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class ShippingCompany(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __ste__(self):
        return self.name

class ShippingCompanyPhone(models.Model):
    shipping_company = models.ForeignKey(ShippingCompany,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

class Order(models.Model):
    order_number = models.IntegerField()
    order_date = models.DateField()
    ship_company = models.ForeignKey(ShippingCompany,on_delete=models.CASCADE)
    customer = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.order_number

class OrderBooks(models.Model):
    order_number = models.ForeignKey(Order,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

