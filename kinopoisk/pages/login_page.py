import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config

class LoginPage(BasePage):
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-tid='loginButton']")
    LOGIN_INPUT = (By.CSS_SELECTOR, "input[name='login']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    USER_AVATAR = (By.CSS_SELECTOR, "div[data-tid='avatar']")

    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.open()
        self.click(self.LOGIN_BUTTON)

    @allure.step("Выполнить логин с логином {login} и паролем {password}")
    def login(self, login, password):
        self.input_text(self.LOGIN_INPUT, login)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Проверить успешную авторизацию")
    def is_logged_in(self):
        return self.is_element_visible(self.USER_AVATAR)
    