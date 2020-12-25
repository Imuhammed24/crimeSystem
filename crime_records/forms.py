from django import forms
from crime_records.models import CrimeRecord, SentencingInfo


class CrimeRecordForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    class Meta:
        model = CrimeRecord
        fields = [
            'first_name', 'last_name', 'middle_name', 'passport',
            'date_of_birth', 'state_of_origin', 'nationality',
            'BVN', 'extra_note',
        ]


class SentencingInfoForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    class Meta:
        model = SentencingInfo
        fields = [
            'date', 'offence', 'entity', 'charge',
            'term',
        ]
