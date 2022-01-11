""" 
Functions that generate Elasticsearch query dictionaries.
"""

class FilterUtils:
    def get_filter_queries(filters):
        """
        Returns a list of query dictionaries for filtering.
            filters: dictionary with the following structure:
                {
                    "<range_fild_name>": (start, end),
                    "<multiple_options_field_name>": [option1, option2, ...],
                    ...
                }
        """
        queries = []
        for field_name, field_value in filters.items():
            if isinstance(field_value, tuple):
                queries.append(
                    {
                        "range": {
                            field_name: {
                                "gte": field_value[0],
                                "lte": field_value[1]
                            }
                        }
                    }
                )
            elif isinstance(field_value, list):
                queries.append(
                    {
                        "terms": {
                            field_name+".keywords": field_value
                        }
                    }
                )
        return queries
        

    def get_query_by_name_filtred(name, filters=None, fuzziness=1):
        """
        Returns a query dictionary for searching by name with.
            name: string.
            filters: dictionary with the following structure:
                {
                    "<range_fild_name>": (start, end),
                    "<multiple_options_field_name>": [option1, option2, ...],
                    ...
                }
            fuzziness: int, default 1.
        """
        must = [
            {
                "multi_match": {
                    "query": name,
                    "fields": [
                        "recipe_title^2",
                        "ingredients^2",
                        "raw_text"
                    ],
                    "type": "most_fields",
                    "fuzziness": fuzziness
                }
            }
        ]
        if filters:
            must.append(get_filter_queries(filters))

        query = {
            "query": {
                "bool": {
                    "must": must
                }
            }
        }
        return query