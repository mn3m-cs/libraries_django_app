from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Libraryy) 
admin.site.register(models.Book)
admin.site.register(models.LibraryPhones)
admin.site.register(models.LibraryAddresses)
admin.site.register(models.LibraryCities)
admin.site.register(models.LibraryCountries)
admin.site.register(models.Category)
admin.site.register(models.LibraryBooks)
admin.site.register(models.Review)
admin.site.register(models.AuthorBooks)
admin.site.register(models.CreditCard)
admin.site.register(models.UserCards)
admin.site.register(models.ShippingCompany)
admin.site.register(models.ShippingCompanyPhone)
admin.site.register(models.Order)
admin.site.register(models.OrderBooks)


