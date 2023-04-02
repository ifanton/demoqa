from components.components import WebElement
from pages.base_page import BasePage


class TextBoxPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.full_name = WebElement(driver, locator='#userName')
        self.current_address = WebElement(driver, locator='#currentAddress')
        self.btn_submit = WebElement(driver, locator='#submit')
        self.submit_output_name = WebElement(driver, locator='#name')
        self.submit_output_address = WebElement(driver, locator='p#currentAddress')
