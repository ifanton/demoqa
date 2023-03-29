from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class WebElement:

    def __init__(self, driver, locator='', text=''):
        self.locator = locator
        self.driver = driver
        self.text = text

    def click(self):  # клик по элементу
        self.find_element().click()

    def find_element(self):  # поиск элемента, метод принимает локатор
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)  # метод возвращает поиск через CSS_SELECTOR

    def find_elements(self):  # поиск сразу нескольких элементов, метод принимает локатор
        time.sleep(3)
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)  # метод возвращает поиск через CSS_SELECTOR

    def check_count_elements(self, count: int):
        if len(self.find_elements()) == count:
            return True
        return False

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def equal_text(self):
        if self.get_text() == self.text:
            return True
        return False

    def visible(self):  # проверка видимости элемента на странице
        return self.find_element().is_displayed()

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def clear(self):
        self.find_element().clear()
