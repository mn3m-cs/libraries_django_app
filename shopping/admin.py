from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.CreditCard)
admin.site.register(models.UserCards)
admin.site.register(models.ShippingCompany)
admin.site.register(models.ShippingCompanyPhone)
admin.site.register(models.Order)
admin.site.register(models.OrderBooks)
