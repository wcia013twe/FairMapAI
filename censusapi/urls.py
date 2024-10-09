from django.urls import path
from censusapi import views

urlpatterns = [
    path('states/', views.state_list, name = 'state_list'),
]