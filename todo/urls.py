"""
Name: Revelle Williams
CIS 218: Assignment 2 - Todo Application
September 25, 2024
"""

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
