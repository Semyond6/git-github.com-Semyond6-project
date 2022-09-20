from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('downloadcsv/', views.DownloadCSV.as_view(), name='downloadCSV'),
    path('search/', views.SearchAddress.as_view(), name='search'),
]