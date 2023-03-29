from components.components import WebElement
from pages.base_page import BasePage


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.first_Name = WebElement(driver, locator='#firstName')
        self.last_Name = WebElement(driver, locator='#lastName')
        self.email = WebElement(driver, locator='#userEmail')
        self.gender_male = WebElement(driver, locator='#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)')
        self.gender_female = WebElement(driver, locator='#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(2)')
        self.gender_other = WebElement(driver, locator='#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(3)')
        self.mobile = WebElement(driver, locator='#userNumber')
        self.birthday = WebElement(driver, locator='#dateOfBirthInput')
