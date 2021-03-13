from django.urls import path
from .views import CreateReview, AddReview

app_name = 'Review'

urlpatterns = [
    # path('add_review/',CreateReview.as_view(),name='add_review'),
    path('add_review/', AddReview.as_view(), name='add_review')
]
