from django.shortcuts import render
from django.views.generic import FormView,CreateView
from .models import UserProfile
from .forms import UserProfileCreatetionForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


class Register(CreateView):
    form_class = UserProfileCreatetionForm
    template_name = 'users/register.html'

    def form_valid(self,form):
        if form.is_valid():
            # save user, so we can use it to add userprofile,...
            form.save(commit=True)
            usrname_form = self.request.POST['username']
            user = User.objects.get(username=usrname_form)
            birth_date = self.request.POST['birth_date']
            gender = self.request.POST['gender']
            is_author = True if 'is_author' in self.request.POST.keys() else False
            country = self.request.POST['country']
            city = self.request.POST['city']
            address = self.request.POST['address']

            user_profile = UserProfile.objects.create(user=user,
                                                      birth_date=birth_date,
                                                      gender=gender,
                                                      is_author=is_author,
                                                     )

            if country != '':
                user_profile.country = country

            if city != '':
                user_profile.city = city

            if address != '':
                user_profile.address = address

            if 'photo' in self.request.FILES.keys():
                user_profile.photo = self.request.FILES['photo']

            user_profile.save()

        return HttpResponseRedirect(reverse('library:home'))