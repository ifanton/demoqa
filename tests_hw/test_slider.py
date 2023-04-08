import allure
import time

from pages.slider_page import SliderPage
from selenium.webdriver import ActionChains


@allure.feature('test_slider')
@allure.story('Передвижение слайдера на заданное значение')
@allure.severity(allure.severity_level.NORMAL)
def test_slider(browser):
    slider_page = SliderPage(browser)
    action_chains = ActionChains(browser)

    slider_page.visit()
    assert slider_page.slider_value.get_dom_attribute('value') == '25'
    while slider_page.slider_value.get_dom_attribute('value') <= '50':
        action_chains.drag_and_drop_by_offset(slider_page.slider_input.find_element(), 1, 0).perform()
        break
    time.sleep(1)
    assert slider_page.slider_value.get_dom_attribute('value') == '50'
