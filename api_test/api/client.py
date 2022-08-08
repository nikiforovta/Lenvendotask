from urllib.parse import urljoin

import requests

from api import paths
from utils.models import JsTestTask


class ResponseStatusCodeException(Exception):
    pass


class JsTestTaskApiClient:
    def __init__(self):
        self.base_url = 'https://www.lenvendo.ru'
        self.session = requests.Session()

    def _request(self, method, url, headers=None, data=None, expected_status=200, params=None):
        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params)
        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"')
        return response

    def get_results(self, search=None, sort_field=None):
        result = list()
        page = 1
        while True:
            response = self.get_result(search, sort_field, page=page)
            products = response['products']
            for item in products:
                result.append(JsTestTask(name=item['name'], image=item['image'], price=item['price']))
            if not response['next_page_url']:
                break
            page += 1
        return result

    def get_result(self, search=None, sort_field=None, page=1):
        path = paths.GET_RESULTS
        query_params = {"page": page}
        if search is not None:
            query_params['search'] = search
        if sort_field is not None:
            query_params['sort_field'] = sort_field
        response = self._request(method='GET', url=urljoin(self.base_url, path), params=query_params)
        return response.json()
