from django.urls import path

from main.apps import MainConfig
from main.views import StudentListView, contacts, StudentCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('materials', StudentCreateView.as_view(), name='create_materials'),
    path('contacts', contacts, name='contacts'),
    path('view/<int:pk>/', StudentDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', StudentUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
]
