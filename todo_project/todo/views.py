"""
Name: Revelle Williams
CIS 218: Assignment 2 - Todo Application
September 25, 2024
"""

from django.views.generic import ListView
from .models import Todo


class HomePageView(ListView):
    """
    View for displaying all Todo items on the home page.
    """

    model = Todo
    template_name = "home.html"
    context_object_name = "todos"
