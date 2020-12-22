from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('account/', include(('account.urls', 'account'), namespace='account')),
    path('crimes/', include(('crime_records.urls', 'crime_records'), namespace='crime_records')),
    path('search/', include(('searches.urls', 'searches'), namespace='searches')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
