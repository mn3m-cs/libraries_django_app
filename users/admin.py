from django.contrib import admin
from . import models


class UserProfileAdmin(admin.ModelAdmin):
    list_filter = ('is_author','is_library_account')

admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.UserprofilePhones)
admin.site.register(models.UserProfileFavourites)
