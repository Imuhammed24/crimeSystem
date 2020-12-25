from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from crime_records.forms import CrimeRecordForm, SentencingInfoForm
from crime_records.models import CrimeRecord, SentencingInfo


def crime_list_view(request):
    records = CrimeRecord.objects.all()
    crime_record_form = CrimeRecordForm()
    # sentencing_info_form = SentencingInfoForm()
    context = {
        'records': records,
        'html_title': 'EXPLORE RECORDS',
        'section': 'explore',
        'add_record_form': crime_record_form,
        # 'sentencing_info_form': sentencing_info_form,
    }
    return render(request, 'crime_records/explore-all.html', context)


def crime_detail_view(request, record_id):
    record = CrimeRecord.objects.get(id=record_id)
    cases = SentencingInfo.objects.filter(criminal=record).all()
    crime_record_form = CrimeRecordForm()
    context = {
        'record': record,
        'html_title': 'RECORD DEATIL VIEW',
        'add_record_form': crime_record_form,
        'section': 'detail',
        'cases': cases,
    }
    return render(request, 'crime_records/record/detail.html', context)


def delete_crime_view(request, record_id):
    record = get_object_or_404(CrimeRecord, id=record_id)
    record.delete()
    return redirect('crime_records:crime_list')


def edit_crime_view(request, record_id):
    record = get_object_or_404(CrimeRecord, id=record_id)
    form = CrimeRecordForm(request.POST or None, request.FILES or None, instance=record)
    sentencing_info_form = SentencingInfoForm(request.POST or None, request.FILES or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Edited Successfully!")
        return redirect('crime_records:crime_list')
    context = {
        'record': record,
        'html_title': 'EDIT RECORD',
        'section': 'edit',
        'main_form': form,
        # 'sentencing_info_form': sentencing_info_form,
    }
    return render(request, 'crime_records/record/edit.html', context)


def add_sentence_view(request, record_id):
    record = get_object_or_404(CrimeRecord, id=record_id)
    sentencing_info_form = SentencingInfoForm()
    if request.method == 'POST':
        sentencing_info_form = SentencingInfoForm(data=request.POST, files=request.FILES or None)
        if sentencing_info_form.is_valid():
            sentencing_info_form.save(commit=False)
            sentencing_info_form.criminal = record
            sentencing_info_form.save()
            messages.success(request, "Added Successfully!")
            return redirect('crime_records:crime_detail', record_id)
    context = {
        'record': record,
        'html_title': 'Add Sentence',
        'section': 'add',
        'main_form': sentencing_info_form,
    }
    return render(request, 'crime_records/record/edit.html', context)


def add_crime_record_view(request):
    if request.method == 'POST':
        form = CrimeRecordForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Added Successfully!")
    return redirect('crime_records:crime_list')
