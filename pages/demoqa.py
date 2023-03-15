from pages.base_page import BasePage  # импорт класса из файла base_page.py - УКАЗЫВАТЬ КАТАЛОГ
from selenium.common.exceptions import NoSuchElementException


class DemoQa(BasePage):  # родительский класс BasePage из файла base_page.py

    def exist_icon(self):  # метод вызывает метод find_element родительского класса BasePage ...
        try:
            self.find_element(locator='#app > header > a')  # ... и передает в него локатор
        except NoSuchElementException:
            return False
        return True

    def click_on_the_icon(self):  # метод возвращает клик по элементу
        self.find_element(locator='#app > header > a').click()  # находим элемент и добавляем клик (.click())

    def equal_url(self):  # создаем метод который сравнивает текущий URL с заданной строкой
        if self.get_url() == 'https://demoqa.com/':
            return True
        else:
            return False
