from django.urls import path
from .views import(
    fetch_data,
    get_skySportNews
)

app_name = 'users'

urlpatterns = [
    path('fetch-news/', fetch_data, name="fetch_data"),
    path('getskysportsnews/', get_skySportNews, name="getskysportnews"),
]
