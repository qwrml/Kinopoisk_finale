import pytest
import allure
from api.kinopoisk_api import KinopoiskAPI

@allure.feature("API Тесты Кинопоиска")
class TestKinopoiskAPI:
    def setup_method(self):
        self.api = KinopoiskAPI()

    @allure.title("Успешный поиск фильма по названию")
    def test_search_movie_success(self):
        response = self.api.search_movie("Паразиты")
        assert response.status_code == 200
        data = response.json()
        assert "docs" in data
        assert len(data["docs"]) > 0

    @allure.title("Поиск с невалидным токеном")
    def test_search_with_invalid_token(self):
        response = self.api.search_with_invalid_token("Паразиты")
        assert response.status_code == 401

    @allure.title("Поиск без токена")
    def test_search_without_token(self):
        response = self.api.search_without_token("Паразиты")
        assert response.status_code == 401

    @allure.title("Поиск с неправильным HTTP методом")
    def test_search_with_wrong_method(self):
        response = self.api.search_with_wrong_method("Паразиты")
        assert response.status_code == 404

    @allure.title("Поиск фильма по несуществующему ID")
    def test_search_movie_by_invalid_id(self):
        response = self.api.get_movie_by_id(250)
        assert response.status_code == 404

    @allure.title("Поиск с пустым запросом")
    def test_search_with_empty_query(self):
        response = self.api.search_movie("")
        data = response.json()
        assert data["total"] == 0

    @allure.title("Успешный поиск фильма по ID")
    def test_get_movie_by_id_success(self):
        response = self.api.search_movie("Паразиты")
        data = response.json()
        if data["docs"]:
            movie_id = data["docs"][0]["id"]
            response = self.api.get_movie_by_id(movie_id)
            assert response.status_code == 200
            movie_data = response.json()
            assert "name" in movie_data

    @allure.title("Поиск с кириллицей в запросе")
    def test_search_cyrillic_query(self):
        response = self.api.search_movie("Паразиты")
        assert response.status_code == 200
        data = response.json()
        assert len(data["docs"]) > 0

    @allure.title("Поиск с латиницей в запросе")
    def test_search_latin_query(self):
        response = self.api.search_movie("Gisaengchung")
        assert response.status_code == 200
        data = response.json()
        assert len(data["docs"]) > 0