import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
    url = "https://qa-scooter.praktikum-services.ru/"
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
