from django.urls import path, include
from . import views



urlpatterns = [
    path('fetch/', views.getNotes),
    path('add/', views.addNotes),
    path('update/<str:pk>/', views.updateNotes),
    path('delete/<str:pk>/', views.deleteNotes)
]