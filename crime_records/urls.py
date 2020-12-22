from django.urls import path
from .views import crime_list_view, crime_detail_view, delete_crime_view

urlpatterns = [
    path('', crime_list_view, name='crime_list'),
    path('<record_id>/', crime_detail_view, name='crime_detail'),
    path('delete/<record_id>/', delete_crime_view, name='delete_crime_record'),
]
