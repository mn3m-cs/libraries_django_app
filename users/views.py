from django.shortcuts import render
from django.views.generic import FormView, CreateView
from .models import UserProfile, UserprofilePhones
from .forms import UserProfileCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Register(CreateView):
    form_class = UserProfileCreationForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        if form.is_valid():
            # save user, so we can use it to add userprofile,...
            # TODO: problem we save user , if any of the next fields is not valid the user is saved already!
            # we need to check all fields before set values
            # OR we delete this user if any of fields is not valid

            usrname_form = self.request.POST['username']
            birth_date = self.request.POST['birth_date']
            gender = self.request.POST['gender']
            is_author = True if 'is_author' in self.request.POST.keys() else False
            is_library_account = True if 'is_library_account' in self.request.POST.keys() else False
            country = self.request.POST['country']
            city = self.request.POST['city']
            address = self.request.POST['address']

            if is_author == True and is_library_account == True:
                # TODO: raise message or error that appears in template
                raise ValidationError("Please choose one 'Author' or 'Library' account.")
            else:
                form.save(commit=True)
                user = User.objects.get(username=usrname_form)
                user_profile = UserProfile.objects.create(user=user,
                                                          birth_date=birth_date,
                                                          gender=gender,
                                                          is_author=is_author,
                                                          is_library_account=is_library_account
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

                if user_profile:
                    phones = [name for name in self.request.POST if name.startswith("phone")]
                    for phone in phones[0:2]:  # Limit: save first two phones only
                        phone = self.request.POST.get(phone)
                        UserprofilePhones.objects.create(userprofile=user_profile, phone=phone)
        # TODO: raise message welcome
        return HttpResponseRedirect(reverse('library:home'))
