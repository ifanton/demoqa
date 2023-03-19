from pages.base_page import BasePage  # импорт класса из файла base_page.py - УКАЗЫВАТЬ КАТАЛОГ
from components.components import WebElement


class DemoQa(BasePage):  # родительский класс BasePage из файла base_page.py

    def __init__(self, driver, text=''):
        self.base_url = 'https://demoqa.com/'
        self.text = text
        super().__init__(driver, self.base_url)  # super прокидывает URL в родительский класс

        self.icon = WebElement(driver, locator='#app > header > a')
        self.btn_elements = WebElement(driver, locator='#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WebElement(driver, locator='#app > footer > span',
                                 text='© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.')

    # все что ниже перенесли в класс WebElement как метод exist
    # def exist_icon(self):  # метод вызывает метод find_element из класса WebElements ...
    #     try:
    #         self.icon.find_element()
    #     except NoSuchElementException:
    #         return False
    #     return True

    # все что ниже удаляем, так как метод "клик" полностью перенесли в класс WebElement
    # def click_on_the_icon(self):  # метод возвращает клик по элементу
    #     self.find_element(locator='#app > header > a').click()  # находим элемент и добавляем клик (.click())
    #
    # def click_on_the_btn_elements(self):  # создаем метод клика на элемент по аналогии с кликом на иконку
    #     self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()

    # # def equal_url(self): перенесли в класс BasePage
