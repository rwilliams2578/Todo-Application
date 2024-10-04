"""
Name: Revelle Williams
CIS 218: Assignment 2 - Todo Application
September 25, 2024
"""

from django.test import TestCase
from django.urls import reverse
from .models import Todo
from datetime import date


class TodoModelTest(TestCase):
    """
    Test case for the Todo model.
    """

    def setUp(self):
        Todo.objects.create(name="Test Todo", complete_by=date.today())

    def test_todo_content(self):
        todo = Todo.objects.get(id=1)
        self.assertEqual(todo.name, "Test Todo")
        self.assertEqual(todo.complete_by, date.today())


class HomePageViewTest(TestCase):
    """
    Test case for the home page view.
    """

    def setUp(self):
        Todo.objects.create(name="Test Todo", complete_by=date.today())

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")

    def test_home_page_contains_correct_content(self):
        resp = self.client.get(reverse("home"))
        self.assertContains(resp, "Test Todo")
        self.assertContains(resp, str(date.today()))
