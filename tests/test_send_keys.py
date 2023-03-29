import time

from selenium.webdriver import Keys

from pages.form_page import FormPage


def test_send_keys(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.first_Name.send_keys('Anton')
    form_page.last_Name.send_keys('Panteleev')
    form_page.email.send_keys('mail@email.com')
    form_page.gender_other.click()
    form_page.gender_female.click()
    form_page.gender_male.click()
    form_page.mobile.send_keys('1234567890')
    form_page.first_Name.clear()
    form_page.last_Name.clear()
    form_page.email.clear()
    form_page.mobile.clear()
    time.sleep(3)
