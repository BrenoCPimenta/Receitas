""" API controller.
"""

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
# from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.elastic_queries import ElasticSearchQueries
from api.filters_utils import FilterUtils


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


#  @api_view(['GET'])
#  def test_route(request):
#  Keeps a test route on the system
#    return Response({"message": "You're on test ground"})
