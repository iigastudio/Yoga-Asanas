
from django.urls import path

from . import views


urlpatterns = [
    path('',  views.getRoutes),
    path('poses/', views.getPoses),
    path('poses/<str:pk>/', views.getPose),
]
