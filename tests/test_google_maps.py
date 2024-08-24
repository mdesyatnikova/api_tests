from models.location import Location


class TestLocation:
    """Создание, изменение и удаление новой локации"""

    def test_create_location(self, client):
        place_id = client.map.create_location(Location())
        response = client.map.get_location(place_id)

    def test_update_location(self, client):
        place_id = client.map.create_location()
        client.map.update_location(place_id, "new address")
        response = client.map.get_location(place_id)

    def test_delete_location(self, client):
        place_id = client.map.create_location()
        response = client.map.delete_location(place_id)
