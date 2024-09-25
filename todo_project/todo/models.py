"""
Name: Revelle Williams
CIS 218: Assignment 2 - Todo Application
September 25, 2024

"""

from django.db import models


class Todo(models.Model):
    """
    Represents a Todo item with a name and completion date.
    """

    name = models.CharField(max_length=200)
    complete_by = models.DateField()

    def __str__(self):
        return self.name
