# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view

from api.elastic_queries import ElasticSearchQueries


class RecipesViewSet(viewsets.ViewSet):
    """
    Responsible for controlling
    elastic recipes
    """

    @action(detail=False, methods=['get'])
    def list_recipes(self, request, pk=None):
        # data = request.data
        queries = ElasticSearchQueries()
        result = queries.search_by_name('ovo')
        return Response(result)


@api_view(['GET'])
def test_route(request):
    """
    Keeps a test route on the system
    """
    return Response({"message": "You're on test ground"})
