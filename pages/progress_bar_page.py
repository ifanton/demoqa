from components.components import WebElement
from pages.base_page import BasePage


class ProgressBarPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.btn_start = WebElement(driver, locator='#startStopButton')
        self.progress_bar = WebElement(driver, locator='#progressBar > div')
