from django.urls import path
from . import views

urlpatterns = [
    path('segregacja/', views.main_page, name='segregation'),
]