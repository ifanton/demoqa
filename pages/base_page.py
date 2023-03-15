from selenium.webdriver.common.by import By
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demoqa.com/'

    def visit(self):  # создаем метод перехода на страницу
        return self.driver.get(self.base_url)  # возвращает переход через .get

    def find_element(self, locator):  # создаем метод поиска элемента, метод принимает локатор
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, locator)  # метод возвращает поиск элемента через CSS_SELECTOR

    def get_url(self):  # создаем метод который возвращает текущий URL
        return self.driver.current_url
