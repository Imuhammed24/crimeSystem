from django.shortcuts import render
from crime_records.models import CrimeRecord


def crime_list_view(request):
    records = CrimeRecord.objects.all()
    context = {
        'records': records,
        'html_title': 'EXPLORE RECORDS',
        'section': 'explore',
    }
    return render(request, 'crime_records/list.html', context)
