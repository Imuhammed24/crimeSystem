from django.shortcuts import render, get_object_or_404
from crime_records.models import CrimeRecord


def crime_list_view(request):
    records = CrimeRecord.objects.all()
    context = {
        'records': records,
        'html_title': 'EXPLORE RECORDS',
        'section': 'explore',
    }
    return render(request, 'crime_records/explore-all.html', context)


def crime_detail_view(request, record_id):
    record = CrimeRecord.objects.get(id=record_id)
    context = {
        'record': record,
        'html_title': 'RECORD DEATIL VIEW',
        'section': 'detail',
    }
    return render(request, 'crime_records/record/detail.html', context)


def delete_crime_view(request, record_id):
    record = get_object_or_404(CrimeRecord, id=record_id)
    record.delete()
    context = {
        'record': record,
        'html_title': 'RECORD DEATIL VIEW',
        'section': 'detail',
    }
    return render(request, 'crime_records/record/detail.html', context)

