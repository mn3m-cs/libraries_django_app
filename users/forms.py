from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,UserprofilePhones,UserProfileFavourites,UserProfileAddresses
from django.contrib.auth.models import User

GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),)

class UserProfileCreatetionForm(UserCreationForm):
    phone = forms.CharField(max_length=20)
    birth_date = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    photo = forms.ImageField(required=False)
    is_author = forms.BooleanField(required=False)
    phone = forms.CharField()
    address = forms.CharField(required=False)
    country  = forms.CharField(required=False)
    city = forms.CharField(required=False)

    class Meta:
        model = User
        # fields =('user','birth_date','gender','photo','is_author')
        fields = ('username','first_name','last_name','email')
