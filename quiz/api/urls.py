from django.urls import path
from .views import APIRequestQuestion


urlpatterns = [
    path('question/', APIRequestQuestion.as_view())
    ]
