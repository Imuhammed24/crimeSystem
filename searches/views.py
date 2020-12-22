from django.shortcuts import render
from .models import SearchQuery
from crime_records.models import CrimeRecord
# Create your views here.


def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        queryset = CrimeRecord.objects.search(query=query)

        context = {
            'queryset': queryset,
            'query': query,
            'section': 'search'
                   }

    return render(request, 'searches/view.html', context)

