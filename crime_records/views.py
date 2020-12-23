from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from crime_records.forms import CrimeRecordForm
from crime_records.models import CrimeRecord


def crime_list_view(request):
    records = CrimeRecord.objects.all()
    crime_record_form = CrimeRecordForm()
    context = {
        'records': records,
        'html_title': 'EXPLORE RECORDS',
        'section': 'explore',
        'add_record_form': crime_record_form
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
    return redirect('crime_records:crime_list')


def add_crime_record_view(request):
    if request.method == 'POST':
        form = CrimeRecordForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Added Successfully!")
    return redirect('crime_records:crime_list')

