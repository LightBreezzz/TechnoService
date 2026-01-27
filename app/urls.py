from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('audit_log/', views.audit_log_view, name='audit_log'),
]