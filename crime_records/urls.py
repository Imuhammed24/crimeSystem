from django.urls import path
from .views import crime_list_view

urlpatterns = [
    path('', crime_list_view, name='crime_list')
]
