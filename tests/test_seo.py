import time

import allure

import pytest

from pages.accordian_page import AccordianPage
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from pages.alerts_page import AlertsPage


@allure.title('test_seo')
@allure.story('Проверка title для нескольких страниц')
def test_seo(browser):
    demo_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    accordian_page = AccordianPage(browser)

    demo_page.visit()
    assert browser.title == demo_page.pageData['title']
    time.sleep(2)
    elements_page.visit()
    assert browser.title == elements_page.pageData['title']
    time.sleep(2)
    accordian_page.visit()
    assert browser.title == accordian_page.pageData['title']


@allure.title('test_check_title_all_pages')
@allure.story('Проверка title для нескольких страниц')
@pytest.mark.parametrize('pages', [DemoQa, AlertsPage])  # декоратор принимает класс и объекты этого класса как атрибуты
def test_check_title_all_pages(browser, pages):  # функция принимает класс как доп атрибут
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.pageData['title'] == page.get_title()
