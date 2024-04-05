# news/tests/test_routes.py
# Импортируем класс HTTPStatus.
from http import HTTPStatus


from django.test import TestCase
# Импортируем функцию reverse().
from django.urls import reverse


class TestRoutes(TestCase):

    def test_home_page(self):
        """Главная страница доступна анонимному пользователю."""
        url = reverse('news:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
