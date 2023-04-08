from components.components import WebElement
from pages.base_page import BasePage


class SliderPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.slider_input = WebElement(driver, '#sliderContainer > div.col-9 > span > input')
        self.slider_value = WebElement(driver, '#sliderValue')
