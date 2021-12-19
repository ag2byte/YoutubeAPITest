from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRecords, name='main'),
    # path('records', views.getRecords, name='records'),
    path('delete', views.clearRecords, name='deleterecords'),
]
