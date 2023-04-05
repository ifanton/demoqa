from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.btn_light = WebElement(driver, locator='div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, locator='#app > header > a')
        self.btn_small_modal = WebElement(driver, locator='#showSmallModal')
        self.btn_close_modal_dialog_small = WebElement(driver, locator='#closeSmallModal')
        self.btn_large_modal = WebElement(driver, locator='#showLargeModal')
        self.btn_close_modal_dialog_large = WebElement(driver, locator='#closeLargeModal')
        self.modal_dialog_show = WebElement(driver, locator='div.fade.modal.show')
