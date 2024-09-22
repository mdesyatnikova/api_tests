from utils.assertions.base import assert_response_value


class TestLocation:
    """Создание, изменение и удаление новой локации"""

    @allure.feature('location')
    @allure.story('create')
    def test_create_location(self, client, data_locations):
        place_id = client.map.create_location(data_locations)
        result = client.map.get_location(place_id)
        assert_response_value(result, "address", data_locations.address)

    @allure.feature('location')
    @allure.story('update')
    def test_update_location(self, client, data_locations):
        place_id = client.map.create_location(data_locations)
        client.map.update_location(place_id, "new address")
        result = client.map.get_location(place_id)
        assert_response_value(result, "address", "new address")

    @allure.feature('location')
    @allure.story('delete')
    def test_delete_location(self, client, data_locations):
        place_id = client.map.create_location(data_locations)
        result = client.map.delete_location(place_id)
        assert_response_value(result, "status", "OK")
