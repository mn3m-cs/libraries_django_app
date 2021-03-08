from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date = models.DateField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='UserProfilePhotos/',blank=True,null=True)
    is_author = models.BooleanField()
    country = models.CharField(null=True,blank=True,max_length=50)
    city = models.CharField(null=True,blank=True,max_length=50)
    address= models.CharField(null=True,blank=True,max_length=50)

    def __str__(self):
        return str(self.user)
    
class UserprofilePhones(models.Model):
    userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.phone

# class UserProfileAddresses(models.Model):
#     userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
#     address = models.CharField(max_length=200)

#     def __str__(self):
#         return self.address

class UserProfileFavourites(models.Model):
    userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    book = models.ForeignKey("library.Book",on_delete=models.CASCADE)

    def __str__(self):
        return self.book
