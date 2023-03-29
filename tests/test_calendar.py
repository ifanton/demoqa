import time
from selenium.webdriver import Keys
from pages.form_page import FormPage


def test_birthday(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.birthday.click()
    form_page.birthday_year.click()
    form_page.birthday_year.send_keys('1986')
    form_page.birthday_month.click()
    form_page.birthday_month.send_keys('March')
    form_page.birthday_month.click()
    form_page.birthday.click_force()
    form_page.birthday.send_keys(Keys.ARROW_LEFT * 9)
    form_page.birthday.send_keys(Keys.BACKSPACE * 2)
    form_page.birthday.send_keys('31')
    form_page.birthday.send_keys(Keys.ENTER)
    time.sleep(5)
