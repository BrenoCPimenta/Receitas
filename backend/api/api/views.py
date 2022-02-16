""" API controller.
"""

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
# from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from api.elastic_queries import ElasticSearchQueries
from api.filters_utils import FilterUtils

from api.authenticate import Authenticate

from api.models import User


def validate_password(password):
    """Validate password.
    """
    if len(password) < 5:
        return False
    return True

class RecipesViewSet(viewsets.ViewSet):
    """
    Elasticsearch recipes controler

    Args:
        Viewset (viewsets.ViewSet): drf class
    """

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Endpoints for search into elasticsearch

        Args:
            request (request): data with request information. Request 
                    parameters: 'name', 'ingredients', 'size', 'page' and 
                    'filters': 'group', 'time_min', 'time_max', 'portions_min', 
                    'portions_max', 'favorites_min', 'favorites_max'.

        Returns:
            Response (drf.response): 200: with elasticsearch result
            400: for not containing correct parameters
            500: for error on elasticsearch search

        """

        try:
            # Read url parameters:
            params = self.request.query_params.dict()
            # Instanciate and exec elasticsearch:
            queries = ElasticSearchQueries()
            
            if 'name' in params:
                if 'page' in params:
                    result = queries.search_by_name(
                        name = params['name'],
                        filters = FilterUtils.generate_filters(params),
                        page = int(params['page'])
                    )
                else:
                    result = queries.search_by_name(
                        name=params['name'],
                        filters=FilterUtils.generate_filters(params)
                    )
                
            elif 'ingredients' in params:
                if 'page' in params:
                    result = queries.search_by_ingredients(
                        ingredients=params['ingredients'].split(','),
                        filters=FilterUtils.generate_filters(params),
                        page=int(params['page'])
                    )
                else:
                    result = queries.search_by_ingredients(
                        ingredients=params['ingredients'].split(','),
                        filters=FilterUtils.generate_filters(params)
                    )

            else:
                return Response(
                        {'ValidationError': 'Wrong parameters passed'},
                        status=status.HTTP_400_BAD_REQUEST)
            return Response(result)

        except Exception as e:
            return Response(
                    {'ValidationError': "Problem on search: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def login(self, request):
        """ 
        Login in website using authentication class.
        """
        try:
            # Read url parameters:
            params = request.POST.dict()

            if not validate_password(params['password']):
                return Response(
                    {'ValidationError': 'Password must be at least 5 characters'},
                    status=status.HTTP_400_BAD_REQUEST)

            # print(params)
            # Instanciate and exec elasticsearch:
            auth = Authenticate(
                username=params['username'],
                password=params['password']
            )
            result = auth.authenticate()
            return Response(result.name)

        except Exception as e:
            return Response(
                    {'ValidationError': "Problem on login: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def register(self, request):
        """ 
        Register in website using User.
        """
        try:
            # Read url parameters:
            params = self.request.POST.dict()
            # print(params)
            # Instanciate and exec elasticsearch:
            user = User(
                username=params['username'],
                password=params['password'],
                email=params['email'],
                name=params['name']
            )
            user.save()
            return Response(True)

        except Exception as e:
            return Response(
                    {'ValidationError': "Problem on register: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
