from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('contacts/', views.contacts, name='contacts'),
    path('thanks/', views.thanks, name='thanks'),
    path('send-request/', views.send_request, name='send_request'),
]