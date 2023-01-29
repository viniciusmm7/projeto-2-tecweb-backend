from django.urls import path

from . import views

urlpatterns = [
    path('api/games/', views.api_games),
    path('api/games/<int:rawgID>/', views.api_game),
]
