from django import forms
from .models import (Book,Libraryy,LibraryAddresses,LibraryPhones,LibraryCities,LibraryCountries)
from django.contrib.auth.models import User
from users.models import UserProfile

class AddLibraryForm(forms.ModelForm):
    address1 = forms.CharField(max_length=200)
    country1 = forms.CharField(max_length=200)
    city1 = forms.CharField(max_length=200)
    phone1 = forms.CharField(max_length=15)
    phone2 = forms.CharField(max_length=15)

    class Meta:
        model = Libraryy
        fields = ['name','lib_email','established_at']  #'owner'


class AddBookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['name','isbn','pub_date','category','price','cover']
        
