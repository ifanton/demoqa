import time
from selenium.webdriver import Keys
from pages.form_page import FormPage


def test_birthday(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.birthday.click()
    form_page.birthday.send_keys(Keys.SHIFT + Keys.HOME)
    form_page.birthday.send_keys('31 Mar 1986')
    form_page.birthday.send_keys(Keys.ENTER)
    time.sleep(5)
