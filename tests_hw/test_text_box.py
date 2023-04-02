from pages.text_box_page import TextBoxPage


def test_text_box(browser):
    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    text_box_page.full_name.send_keys('Bill Gates')
    text_box_page.current_address.send_keys('California')
    text_box_page.btn_submit.click_force()
    assert text_box_page.submit_output_name.get_text() == 'Name:Bill Gates'
    assert text_box_page.submit_output_address.get_text() == 'Current Address :California'
