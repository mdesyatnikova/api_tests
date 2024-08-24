import requests

from base.google_maps_api import GoogleMapsAPI


class Client:
    def __init__(self, base_url):
        self.base_url = base_url
        self.map = GoogleMapsAPI(self)

    def get(self, url, params=None, headers=None, auth=None):
        result = requests.get(url, params=params, headers=headers, auth=auth, verify=False)
        return result

    def post(self, url, body, params=None, headers=None, auth=None):
        result = requests.post(url, json=body, params=params, headers=headers, auth=auth, verify=False)
        return result

    def put(self, url, body, params=None, headers=None, auth=None):
        result = requests.put(url, json=body, params=params, headers=headers, auth=auth, verify=False)
        return result

    def delete(self, url, body, params=None, headers=None, auth=None):
        result = requests.delete(url, json=body, params=params, headers=headers, auth=auth, verify=False)
        return result
