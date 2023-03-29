import time

from pages.form_page import FormPage


def test_send_keys(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_Name.send_keys('Anton')
    form_page.last_Name.send_keys('Panteleev')
    form_page.email.send_keys('mail@email.com')
    form_page.gender_male.click()
    form_page.mobile.send_keys('1234567890')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(5)
    assert form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.btn_close_modal.click_force()
