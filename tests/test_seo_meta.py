import time

import allure

import pytest

from pages.accordian_page import AccordianPage
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTabPage
from pages.alerts_page import AlertsPage


@allure.title('test_seo_meta')
@allure.story('Проверка meta для нескольких страниц')
@pytest.mark.parametrize('pages', [DemoQa, AlertsPage, BrowserTabPage, AccordianPage])
def test_seo_meta(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.meta.exist()
    assert page.meta.get_dom_attribute('name') == 'viewport'
    assert page.meta.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
