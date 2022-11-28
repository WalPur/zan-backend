from rest_framework.views import APIView
from rest_framework.response import Response

import requests
import json

class Trudvsem(APIView):
    def get(self, request, format=None):
        response = {}
        r = requests.get(
            'https://trudvsem.ru/iblocks/_catalog/flat_filter_prr_search_vacancies/data?filter=%7B%22regionCode%22%3A%5B%221400000000000%22%5D%2C%22salary%22%3A%5B%220%22%2C%22999999%22%5D%2C%22scheduleType%22%3A%5B%22FULL%22%5D%2C%22busyType%22%3A%5B%22FULL%22%5D%7D&orderColumn=RELEVANCE_DESC&page=0&pageSize=10'
        )
        r_status = r.status_code
        print(str(r.text))
        if r_status == 200:
            data = json.loads(str(r.text))
            response = data
            response['status'] = 200
            response['message'] = 'success'
        else:
            response['status'] = r.status_code
            response['message'] = 'error'
            response['credentials'] = {}
        return Response(response)