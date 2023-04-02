import time

from selenium.webdriver import Keys

from pages.form_page import FormPage


def test_login_form_state_and_city(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.state.click_force()
    form_page.state.send_keys(Keys.ARROW_DOWN)
    # form_page.state.send_keys('NCR')
    form_page.state.send_keys(Keys.ENTER)
    form_page.city.click_force()
    form_page.city.send_keys(Keys.ARROW_DOWN)
    # form_page.city.send_keys('Delhi')
    form_page.city.send_keys(Keys.ENTER)
    form_page.btn_submit.click_force()
    time.sleep(5)
