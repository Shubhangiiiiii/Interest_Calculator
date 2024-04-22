from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_interest, name='calculate_interest'),
]