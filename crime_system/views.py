from django.shortcuts import render


def index_view(request):
    context = {'html_title': 'CRIME MANAGEMENT SYSTEM'}
    return render(request, 'index.html', context)
