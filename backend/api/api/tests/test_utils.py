
from rest_framework.test import APIClient
from rest_framework import status
#from django.core.urlresolvers import reverse
from django.urls import reverse

from django.test import TestCase

from api.filters_utils import FilterUtils

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def test_generate_filters_no_param(self):
        """Test the generate_filters function with no parameters."""
        params = {}
        filters = None
        self.assertEqual(
            FilterUtils.generate_filters(params),
            filters)
        
    def test_generate_filters_all_params(self):
        """Test the generate_filters function with all parameters."""
        params = {
            'group': 'sopas',
            'time_min': 1,
            'time_max': 2,
            'portions_min': 3,
            'portions_max': 4,
            'favorites_min': 5,
            'favorites_max': 6,
        }
        filters = {
            'group': ['Sopas'],
            'preparation_time': (1, 2),
            'portions': (3, 4),
            'favorites': (5, 6)
        }
        self.assertEqual(
            FilterUtils.generate_filters(params),
            filters)


    # def set_response(self, url, param):
    #     """Create response from parameter"""
    #     client = APIClient()
    #     return client.get(
    #         url,
    #         param,
    #         format='json')

    # def test_api_wrong_url(self):
    #     """Test the api has handle wrong url capability."""
    #     wrong_url = '/any'
    #     wrong_param = {'ingredient': 'tomate'}
    #     self.assertEqual(
    #         self.set_response(wrong_url, wrong_param).status_code,
    #         status.HTTP_404_NOT_FOUND)

    # def test_api_recipes_list_wrong_param(self):
    #     """Test the api has handle wrong parameters capability."""
    #     url = '/recipes/'
    #     param = {'wrong': 'even more wrong'}
    #     self.assertEqual(
    #         self.set_response(url, param).status_code,
    #         status.HTTP_400_BAD_REQUEST)
