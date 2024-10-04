"""
Name: Revelle Williams
CIS 218: Assignment 2 - Todo Application
September 25, 2024
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo.urls")),
]
