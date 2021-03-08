from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import Register

app_name = 'users'

urlpatterns=[
    path('login/',LoginView.as_view(template_name='users/login.html',
                                    redirect_authenticated_user=True)
                                    ,name='login'),

    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',Register.as_view(success_url='/home'),name='register'),
    
]