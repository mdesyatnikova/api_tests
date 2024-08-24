import allure
import requests

from base.google_maps_api import GoogleMapsAPI


class Client:
    def __init__(self, base_url):
        self.base_url = base_url
        self.map = GoogleMapsAPI(self)

    @allure.step('Making GET request to "{url}"')
    def get(self, url, params=None, headers=None, auth=None):
        result = requests.get(url, params=params, headers=headers, auth=auth, verify=False)
        return result

    @allure.step('Making POST request to "{url}"')
    def post(self, url, body, params=None, headers=None, auth=None):
        result = requests.post(url, json=body, params=params, headers=headers, auth=auth, verify=False)
        return result

    @allure.step('Making PUT request to "{url}"')
    def put(self, url, body, params=None, headers=None, auth=None):
        result = requests.put(url, json=body, params=params, headers=headers, auth=auth, verify=False)
        return result

    @allure.step('Making DELETE request to "{url}"')
    def delete(self, url, body, params=None, headers=None, auth=None):
        result = requests.delete(url, json=body, params=params, headers=headers, auth=auth, verify=False)
        return result
