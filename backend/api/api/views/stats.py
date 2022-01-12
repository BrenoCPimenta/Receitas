""" API controller.
"""

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
# from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.elastic_queries import ElasticSearchQueries
from api.filters_utils import FilterUtils


class StatsViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def stats(self, request):
        mocked_data = [{ "idFeedback": 0, "idUser": 1, "search": "Salmão", "type": "ingrediente", "date": "2021-10-14T22:34:09.821Z", "feedback": 4 }, { "idFeedback": 1, "idUser": 1, "search": "Risoto e", "type": "textual", "date": "2021-04-01T00:18:17.994Z", "feedback": 2 }, { "idFeedback": 2, "idUser": 1, "search": "de seco segundo Sul", "type": "textual", "date": "2021-01-27T15:00:43.835Z", "feedback": 4 }, { "idFeedback": 3, "idUser": 1, "search": "Patê com Sul e", "type": "textual", "date": "2021-08-24T01:39:33.620Z", "feedback": 1 }, { "idFeedback": 4, "idUser": 1, "search": "Light", "type": "ingrediente", "date": "2021-05-29T21:41:09.399Z", "feedback": 5 }, { "idFeedback": 5, "idUser": 1, "search": "do rúcula linguiça", "type": "ingrediente", "date": "2021-06-30T00:45:11.720Z", "feedback": 4 }, { "idFeedback": 6, "idUser": 1, "search": "à feijão tomate seco do", "type": "textual", "date": "2021-08-13T21:56:46.973Z", "feedback": 2 }, { "idFeedback": 7, "idUser": 1, "search": "à Patê rúcula", "type": "textual", "date": "2021-12-08T06:14:16.212Z", "feedback": 3 }, { "idFeedback": 8, "idUser": 1, "search": "Tam", "type": "ingrediente", "date": "2021-02-03T06:27:49.373Z", "feedback": 1 }, { "idFeedback": 9, "idUser": 1, "search": "Patê e", "type": "textual", "date": "2021-04-14T13:10:40.603Z", "feedback": 3 }, { "idFeedback": 10, "idUser": 1, "search": "", "type": "textual", "date": "2021-08-22T07:50:40.152Z", "feedback": 5 }, { "idFeedback": 11, "idUser": 1, "search": "", "type": "ingrediente", "date": "2021-10-12T11:47:55.480Z", "feedback": 5 }, { "idFeedback": 12, "idUser": 1, "search": "", "type": "ingrediente", "date": "2021-09-09T10:38:53.979Z", "feedback": 5 }, { "idFeedback": 13, "idUser": 1, "search": "e", "type": "ingrediente", "date": "2021-11-19T04:37:04.398Z", "feedback": 1 }, { "idFeedback": 14, "idUser": 1, "search": "Carreteiro seco, seco e Penne", "type": "textual", "date": "2021-01-20T18:42:15.408Z", "feedback": 5 }, { "idFeedback": 15, "idUser": 1, "search": "Macarrão e", "type": "ingrediente", "date": "2021-06-10T23:06:43.333Z", "feedback": 4 }, { "idFeedback": 16, "idUser": 1, "search": "Arroz queijo", "type": "textual", "date": "2021-10-29T14:49:18.242Z", "feedback": 4 }, { "idFeedback": 17, "idUser": 1, "search": "de seco Arroz linguiça", "type": "ingrediente", "date": "2021-06-14T12:34:31.418Z", "feedback": 1 }]
        return Response(data=mocked_data)