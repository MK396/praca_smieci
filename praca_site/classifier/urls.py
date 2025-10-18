from django.urls import path
from . import views

urlpatterns = [
    path('klasyfikacja/', views.classify_image, name='classify'),
]
