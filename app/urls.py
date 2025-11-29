from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('print-outsourcing/', views.print_outsourcing, name='print_outsourcing'),
    path('it-outsourcing/', views.it_outsourcing, name='it_outsourcing'),
    path('software-solutions/', views.software_solutions, name='software_solutions'),
]