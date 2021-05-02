from django.urls import path
from .views import crime_list_view, crime_detail_view, delete_crime_view,\
    add_crime_record_view, edit_crime_view, add_sentence_view

urlpatterns = [
    path('', crime_list_view, name='crime_list'),
    path('add/', add_crime_record_view, name='add_crime_record'),
    path('add-sentence/<record_id>/', add_sentence_view, name='add_sentence'),
    path('<record_id>/', crime_detail_view, name='crime_detail'),
    path('delete/<record_id>/', delete_crime_view, name='delete_crime_record'),
    path('edit/<record_id>/', edit_crime_view, name='edit_crime_record'),
]

