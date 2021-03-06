from django.urls import path
from library import views
from rest_framework.urlpatterns import format_suffix_patterns
from .rest_view import Libraries,AddLibraryBookAPIView

app_name='library'

urlpatterns = [
    path('home/',views.HomeView.as_view(),name='home'),
    path('add_library/',views.AddLibrary.as_view(),name='add_library'),
    path('add_book/',views.AddBook.as_view(success_url='/home/'),name='add_book'),

    #API
    path('libraries_list_api/',Libraries.as_view(),name='list_libraries'),
    path('add_library_books/',AddLibraryBookAPIView.as_view(),name='add_library_books'),
] 

urlpatterns = format_suffix_patterns(urlpatterns)
