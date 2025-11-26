from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.config import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open(self):
        self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
        