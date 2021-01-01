from django.urls import path
from .views import BoothView


urlpatterns = [
    path('<str:voting_url>/', BoothView.as_view()),
]
