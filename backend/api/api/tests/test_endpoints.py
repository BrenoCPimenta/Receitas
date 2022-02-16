
from rest_framework.test import APIClient
from rest_framework import status
#from django.core.urlresolvers import reverse
from django.urls import reverse

from django.test import TestCase


class ViewTestCase(TestCase):
    """Test suite for the api views."""


    def set_response(self, url, param):
        """Create response from parameter"""
        client = APIClient()
        return client.get(
            url,
            param,
            format='json')

    def set_response_post(self, url, param):
        """Create response from parameter"""
        client = APIClient()
        return client.post(
            url,
            param)

    def test_api_wrong_url(self):
        """Test the api has handle wrong url capability."""
        wrong_url = '/any'
        wrong_param = {'ingredient': 'tomate'}
        self.assertEqual(
            self.set_response(wrong_url, wrong_param).status_code,
            status.HTTP_404_NOT_FOUND)

    def test_api_recipes_list_wrong_param(self):
        """Test the api has handle wrong parameters capability."""
        url = '/recipes/search/'
        param = {'wrong': 'even more wrong'}
        self.assertEqual(
            self.set_response(url, param).status_code,
            status.HTTP_400_BAD_REQUEST)

    def test_register_and_login(self):
        """Test the api has register and login capability."""
        url = '/recipes/register/'
        param = {'username': 'test', 'password': 'testpass', 'email': 'test@test.com', 'name': 'test'}
        self.assertTrue(self.set_response_post(url, param))

        url='/recipes/login/'
        param = {'username': 'test', 'password': 'testpass'}
        self.assertEqual(self.set_response_post(url, param).json(), 'test')

    def test_bad_regiter(self):
        url = '/recipes/register/'
        param = {'username': 'test', 'password': 'test', 'email': 'test@test.com', 'name': 'test'}
        self.assertEqual(self.set_response_post(url, param).status_code, status.HTTP_400_BAD_REQUEST)
