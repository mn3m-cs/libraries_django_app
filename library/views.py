from django.shortcuts import render
from .models import (LibraryBooks,Book,Libraryy,LibraryAddresses,
LibraryPhones,LibraryCities,LibraryCountries,AuthorBooks)
from .forms import AddLibraryForm,AddBookForm
from users.models import UserProfile
import re
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView,CreateView,FormView
from django.http import HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin

class HomeView(ListView):
    model = Book
    template_name = 'library/home.html'
    context_object_name = 'LibBooks'
    
class AddLibrary(CreateView):
    form_class=AddLibraryForm
    template_name = 'library/library_form.html'

    def form_valid(self,form):
        if form.is_valid():
            up = UserProfile.objects.get(user=self.request.user)
            instance = form.save(commit=False)
            instance.owner = up
            # self.object = form.save()


        # form.save(commit=False)
        # user_profile = UserProfile.objects.get(user=self.request.user)
        # self.request.POST._mutable = True
        # self.request.POST['owner'] = user_profile
        # library = self.request.POST 
        # print(library)

        form.save(commit=True)
        lib_name = self.request.POST.get('name')
        library = Libraryy.objects.get(name=lib_name)
        if library:
            #get list of phones and add it to LibraryPhones Table.
            phones = [name for name in self.request.POST if name.startswith("phone")]
            for phone in phones:
                phone = self.request.POST.get(phone)
                LibraryPhones.objects.create(library=library,phone=phone)

            #get list of addresses and add it to LibraryAddresses Table.
            addresses = [name for name in self.request.POST if name.startswith("address")]
            for address in addresses:
                address = self.request.POST.get(address)
                LibraryAddresses.objects.create(library=library,address=address)
            
            #get list of countries and add it to LibraryCountries Table.
            countries = [name for name in self.request.POST if name.startswith("country")]
            for country in countries:
                country = self.request.POST.get(country)
                LibraryCountries.objects.create(library=library,country=country)

            #get list of cities and add it to Librarycities Table.
            cities = [name for name in self.request.POST if name.startswith("city")]
            for city in cities:
                city = self.request.POST.get(city)
                LibraryCities.objects.create(library=library,city=city)

        return super(AddLibrary,self).form_valid(form)
    
class AddBook(LoginRequiredMixin,UserPassesTestMixin,FormView):
    # model = Book
    form_class = AddBookForm
    template_name = 'library/book_form.html'
    #TODO: ADD login_url
    def test_func(self):
        ''' only admins can see this view'''
        return UserProfile.objects.get(user=self.request.user).is_author

    def form_valid(self, form):
        print(self.request.POST)
        if form.is_valid():
            up = UserProfile.objects.get(user=self.request.user)
            instance = form.save(commit=False)
            instance.author = up
            self.object = form.save()
            AuthorBooks.objects.create(author=up,book=self.object)
            
        return super(AddBook, self).form_valid(form)
