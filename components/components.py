from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class WebElement:

    def __init__(self, driver, locator='', text=''):
        self.locator = locator
        self.driver = driver
        self.text = text

    def find_element(self):  # поиск элемента, метод принимает локатор
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)  # метод возвращает поиск через CSS_SELECTOR

    def find_elements(self):  # поиск сразу нескольких элементов, метод принимает локатор
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)  # метод возвращает поиск через CSS_SELECTOR

    def click(self):  # клик по элементу
        self.find_element().click()

    def click_force(self):
        self.driver.execute_script('arguments[0].click();', self.find_element())

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
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True
