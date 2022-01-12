""" 
Definition of elasticsearch class.

Connects to elasticsearch and performs search
by ingredients and recipe names.

Typical usage example:

  queries = ElasticSearchQueries()
  ingredients_info = queries.search_by_ingredients([ingredients])
  recipe_info = result = queries.search_by_ingredients(name)
"""
import elasticsearch as es

from api.filters_utils import FilterUtils

def parse_result(result):
    """
    Parses the result from elasticsearch. Returns the contens inside _source
    for each result.
        result: dict.
    """
    data = []
    for hit in result['hits']['hits']:
        data.append(hit['_source'])
    return data


class ElasticSearchQueries:
    """
    Class that handle elasticsearch queries.
    """
    def __init__(self, host='localhost', port=9200, index='recipes'):
        """
        Initializes the class.
            host: string, default 'localhost'
                Elasticsearch host.
            port: int, default 9200
                Elasticsearch port.
            index: string, default 'recipes'
                Elasticsearch index that contains the recipes' data.
        """
        self.host = host
        self.port = port
        self.index = index
        self.es = es.Elasticsearch([{'host': self.host, 'port': self.port}])
        self.returning_fields = [
            'recipe_title',
            'page_title',
            'link',
            'images',
            'raw_text',
            'group',
            'comments',
            'favorites',
            'preparation_time'
            'portions'
        ]

    def reset_returning_fields(self, fields):
        """
        Resets the returning fields.
            fields: list of strings.
        """
        self.returning_fields = fields

    def search_by_name(self, name, filters = None, size=12, page=1, return_raw=False):
        """
        Search for recipes by name.
            name: string.
            filters: dictionary with the following structure:
                {
                    "<range_fild_name>": (start, end),
                    "<multiple_options_field_name>": [option1, option2, ...],
                    ...
                }
            size: int, default 10
                Number of results to return.
            page: int, default 1.
            return_raw: bool, default False
                If true, returns the raw result from elasticsearch.
        """
        query = FilterUtils.get_query_by_name_filtred(name, filters)
        response = self.es.search(
            index=self.index,
            body=query,
            size=size,
            from_=size*(page-1),
            _source=self.returning_fields
        )

        if return_raw:
            return response
        return parse_result(response)

    def search_by_ingredients(self, ingredients, filters=None, size=12, page=1, return_raw=False):
        """
        Search for recipes by ingredients.
            ingredients: list of strings.
            size: int, default 10
                Number of results to return.
            page: int, default 1.
            return_raw: bool, default False
                If true, returns the raw result from elasticsearch.
        """
        query = FilterUtils.get_query_by_ingredients_filtred(ingredients, filters)
        response = self.es.search(
            index=self.index,
            body=query,
            size=size,
            from_=size*(page-1),
            _source=self.returning_fields
        )

        if return_raw:
            return response
        return parse_result(response)
