from django.db import models
from library.models import UserProfile,Book

class CreditCard(models.Model):
    card_number = models.CharField(max_length=14, unique=True)
    expxire_date = models.DateField()

    # card_type = models.

    def __str__(self):
        return self.card_number


class UserCards(models.Model):
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class ShippingCompany(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __ste__(self):
        return self.name


class ShippingCompanyPhone(models.Model):
    shipping_company = models.ForeignKey(ShippingCompany, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)


class Order(models.Model):
    order_number = models.IntegerField()
    order_date = models.DateField()
    ship_company = models.ForeignKey(ShippingCompany, on_delete=models.CASCADE)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_number


class OrderBooks(models.Model):
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
