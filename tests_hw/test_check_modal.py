import allure
import pytest

from pages.modal_dialogs_page import ModalDialogs


@allure.title('tests_check_modal')
@allure.story('Проверка модальных окон')
# @pytest.mark.skipif(condition='')
def test_check_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)

    modal_dialogs_page.visit()
    assert modal_dialogs_page.btn_small_modal.exist()
    assert modal_dialogs_page.btn_large_modal.exist()
    modal_dialogs_page.btn_small_modal.click()
    assert modal_dialogs_page.modal_dialog_show.visible()
    modal_dialogs_page.btn_close_modal_dialog_small.click()
    assert not modal_dialogs_page.modal_dialog_show.exist()
    modal_dialogs_page.btn_large_modal.click()
    assert modal_dialogs_page.modal_dialog_show.visible()
    modal_dialogs_page.btn_close_modal_dialog_large.click()
    assert not modal_dialogs_page.modal_dialog_show.exist()
