from django.urls import include, path
from .views import check_imei, check_wite_list


list_urls = [
    path('check-imei/', check_imei, name='check_imei'),
    path('white-list/', check_wite_list, name='check_wite_list')
]


urlpatterns = [
    path('', include(list_urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
