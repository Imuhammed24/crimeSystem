from django.urls import path
from .views import crime_list_view, crime_detail_view

urlpatterns = [
    path('', crime_list_view, name='crime_list'),
    path('<record_id>/', crime_detail_view, name='crime_detail'),
]
