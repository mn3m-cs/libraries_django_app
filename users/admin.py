from django.contrib import admin
from . import models
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_filter = ('is_author',)

admin.site.register(models.UserProfile,UserProfileAdmin)
admin.site.register(models.UserprofilePhones)
admin.site.register(models.UserProfileAddresses)
admin.site.register(models.UserProfileFavourites)

