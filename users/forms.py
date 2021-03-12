from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, UserprofilePhones
# UserProfileFavourites,UserProfileAddresses
from django.contrib.auth.models import User

GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),)


class UserProfileCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=20)
    birth_date = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    photo = forms.ImageField(required=False)
    phone1 = forms.CharField(required=False)
    address = forms.CharField(required=False)
    country = forms.CharField(required=False)
    city = forms.CharField(required=False)
    is_author = forms.BooleanField(required=False)
    is_library_account = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    # Later TODO: add widget to is_author + is_library account as ===> radio button
