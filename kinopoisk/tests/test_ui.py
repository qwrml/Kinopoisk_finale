import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.base_page import BasePage
from pages.login_page import LoginPage
from config.config import Config

@allure.feature("UI Тесты Кинопоиска")
class TestKinopoiskUI:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Проверка открытия главной страницы")
    def test_open_main_page(self):
        with allure.step("Открыть главную страницу"):
            self.base_page.open()
        
        with allure.step("Проверить заголовок страницы"):
            assert "Кинопоиск" in self.driver.title

    @allure.title("Поиск фильма через UI")
    def test_search_movie(self):
        with allure.step("Открыть главную страницу"):
            self.base_page.open()
        
        with allure.step("Найти поле поиска и ввести название фильма"):
            search_input = (By.CSS_SELECTOR, "input[name='kp_query']")
            self.base_page.input_text(search_input, "Паразиты")
        
        with allure.step("Нажать кнопку поиска"):
            search_button = (By.CSS_SELECTOR, "button[type='submit']")
            self.base_page.click(search_button)
        
        with allure.step("Проверить результаты поиска"):
            results = (By.CSS_SELECTOR, ".search_results")
            assert self.base_page.find_element(results)

    @allure.title("Проверка элементов главной страницы")
    def test_main_page_elements(self):
        with allure.step("Открыть главную страницу"):
            self.base_page.open()
        
        with allure.step("Проверить наличие логотипа"):
            logo = (By.CSS_SELECTOR, ".styles_logo__aXBXG")
            assert self.base_page.is_element_visible(logo)

    @allure.title("Тест авторизации")
    def test_login(self):
        with allure.step("Открыть страницу логина"):
            self.login_page.open_login_page()
        
        with allure.step("Выполнить авторизацию"):
            self.login_page.login(Config.LOGIN, Config.PASSWORD)
        
        with allure.step("Проверить успешную авторизацию"):
            assert self.login_page.is_logged_in()

    @allure.title("Поиск иностранного фильма по оригинальному названию")
    def test_search_foreign_movie(self):
        with allure.step("Открыть главную страницу"):
            self.base_page.open()
        
        with allure.step("Найти поле поиска и ввести оригинальное название"):
            search_input = (By.CSS_SELECTOR, "input[name='kp_query']")
            self.base_page.input_text(search_input, "Instant Family")
        
        with allure.step("Нажать кнопку поиска"):
            search_button = (By.CSS_SELECTOR, "button[type='submit']")
            self.base_page.click(search_button)
        
        with allure.step("Проверить результаты поиска"):
            results = (By.CSS_SELECTOR, ".search_results")
            assert self.base_page.find_element(results)
            