# from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.elastic_queries import ElasticSearchQueries


class RecipesViewSet(viewsets.ViewSet):
    """
    Responsible for controlling
    elastic recipes
    """
    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        try:
            # Read url parameters:
            params = self.request.query_params.dict()
            # Instanciate and exec elasticsearch:
            queries = ElasticSearchQueries()
            if 'name' in params:
                if 'pagination' in params:
                    result = queries.search_by_name(
                                name=params['name'],
                                size=params['paginatio'])
                else:
                    result = queries.search_by_name(name=params['name'])
            elif 'ingredients' in params:
                if 'pagination' in params:
                    result = queries.search_by_ingredients(
                                ingredients=params['ingredients'].split(','),
                                size=params['paginatio'])
                else:
                    result = queries.search_by_ingredients(
                                ingredients=params['ingredients'].split(','))
            else:
                return Response(
                        {'ValidationError': 'Wrong parameters passed'},
                        status=status.HTTP_400_BAD_REQUEST)
            return Response(result)

        except Exception as e:
            # log(e)
            return Response(
                    {'ValidationError': "Problem on search: \n"+ str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def test_route(request):
    """
    Keeps a test route on the system
    """
    return Response({"message": "You're on test ground"})
