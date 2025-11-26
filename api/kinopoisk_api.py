import requests
import allure
from config.config import Config

class KinopoiskAPI:
    def __init__(self):
        self.base_url = Config.API_URL
        self.headers = {
            "X-API-KEY": Config.API_KEY,
            "Content-Type": "application/json"
        }

    @allure.step("Поиск фильма по названию: {query}")
    def search_movie(self, query):
        url = f"{self.base_url}/movie/search"
        params = {"query": query}
        response = requests.get(url, headers=self.headers, params=params)
        return response

    @allure.step("Получить фильм по ID: {movie_id}")
    def get_movie_by_id(self, movie_id):
        url = f"{self.base_url}/movie/{movie_id}"
        response = requests.get(url, headers=self.headers)
        return response

    @allure.step("Поиск с невалидным токеном: {query}")
    def search_with_invalid_token(self, query):
        url = f"{self.base_url}/movie/search"
        headers = {"X-API-KEY": "invalid_token", "Content-Type": "application/json"}
        response = requests.get(url, headers=headers, params={"query": query})
        return response

    @allure.step("Поиск без токена: {query}")
    def search_without_token(self, query):
        url = f"{self.base_url}/movie/search"
        headers = {"Content-Type": "application/json"}
        response = requests.get(url, headers=headers, params={"query": query})
        return response

    @allure.step("Поиск с неправильным методом: {query}")
    def search_with_wrong_method(self, query):
        url = f"{self.base_url}/movie/search"
        response = requests.put(url, headers=self.headers, params={"query": query})
        return response