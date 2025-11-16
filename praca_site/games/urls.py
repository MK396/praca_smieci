from django.urls import path
from . import views

urlpatterns = [
    path('gra/', views.main_page_games, name='games'),
]