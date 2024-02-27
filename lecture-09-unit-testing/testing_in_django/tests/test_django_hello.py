from django.test import TestCase


class HelloTest(TestCase):

    def test_first(self):
        self.assertEqual(10, 10)
