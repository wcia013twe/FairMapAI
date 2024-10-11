from django.urls import path
from censusapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('states/', views.state_list, name = 'state_list'),
    path('states/<int:state_id>/', views.state_detail, name='state_detail'),
    # path('states/<int:state_id>/districts/<int:district_id>', views.district_detail, name = 'district_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)