from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRecords, name='main'),
    path('delete', views.clearRecords, name='deleterecords'),
]
