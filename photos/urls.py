from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from photos import views

urlpatterns = [
    path('photos', views.PhotoListCreateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
