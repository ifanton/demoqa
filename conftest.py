import pytest
from selenium import webdriver


@pytest.fixture(scope="session")  # создание фикстуры для запуска драйвера браузера
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
