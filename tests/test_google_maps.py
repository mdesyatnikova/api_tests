class TestLocation:
    """Создание, изменение и удаление новой локации"""
    def test_create_location(self, client):
        client.map.create_location()
