from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/printers/', views.catalog_printers, name='catalog_printers'),
    path('about/', views.about, name='about'),
    path('cases/', views.cases, name='cases'),
    path('contacts/', views.contacts, name='contacts'),
]