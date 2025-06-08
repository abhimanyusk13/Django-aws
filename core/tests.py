from django.test import TestCase
from .models import Example


class ExampleModelTest(TestCase):
    """Basic test for the Example model."""

    def test_str(self):
        obj = Example.objects.create(name="demo")
        self.assertEqual(str(obj), "demo")
