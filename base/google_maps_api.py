from http import HTTPStatus

import allure
import requests

from models.location import Location
from utils.assertions.base import assert_status_code
from utils.constant.resource import Locations


class GoogleMapsAPI:
    def __init__(self, client):
        self.client = client
        self.key = {'key': "qaclick123"}

    @allure.step("Creating location")
    def create_location(self, body=Location()):
        """Создание локации"""
        response = self.client.post(self.client.base_url + Locations.ADD, params=self.key,
                                    body=body.model_dump(by_alias=True, exclude_none=True))
        assert_status_code(response.status_code, HTTPStatus.OK)

        return response

    @allure.step("Getting location with place_id {place_id}")
    def get_location(self, place_id):
        """Получение локации"""
        get_loc_params = self.key | {'place_id': place_id}
        response = requests.get(self.client.base_url + Locations.GET, params=get_loc_params)
        assert_status_code(response.status_code, HTTPStatus.OK)
        result = response.json()
        return result

    @allure.step("Deleting location with place_id {place_id}")
    def delete_location(self, place_id):
        """Удаление локации"""
        delete_loc_json = {'place_id': place_id}
        response = requests.get(self.client.base_url + Locations.DELETE, params=self.key, json=delete_loc_json)
        assert_status_code(response.status_code, HTTPStatus.OK)
        result = response.json()
        return result
