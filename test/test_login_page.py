import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from pages.login_page import RegistrationPageScooter


class TestRegistrationPageScooter:
    test_data_1 = ["Екатерина", "Никитина", "Пятницкая", "Пражская", "+79999999999"]
    test_data_2 = ["Иван", "Иванов", "Треугольная", "Пражская", "+78888888888"]

    @allure.title('Заказать самокат через кнопку "Заказать" вверху страницы')
    @allure.description(
        "Заполнить форму заказа и проверить что появилось всплывающее окно с сообщение об успешном создании заказа"
    )
    @pytest.mark.parametrize("name,last_name,street,subway,phone", [test_data_1, test_data_2])
    # Заказать самокат через кнопку "Заказать" вверху страницы
    def test_registration_scooter_order_up(self, driver, name, last_name, street, subway, phone):
        rent_scooter_page = RegistrationPageScooter(driver)
        # кликнуть на кнопку да все привыкли
        rent_scooter_page.click_cookie()
        # заполняю поля формы страницы заказа
        rent_scooter_page.create_order(name, last_name, street, subway, phone, rent_scooter_page.order_up)
        # заполняю поля формы страницы аренды
        rent_scooter_page.create_rent()

    @allure.title('Заказать самокат через кнопку "Заказать" в середине страницы')
    @allure.description(
        "Заполнить форму заказа и проверить что появилось всплывающее окно с сообщение об успешном создании заказа"
    )
    @pytest.mark.parametrize("name,last_name,street,subway,phone", [test_data_1, test_data_2])
    # Заказать самокат через кнопку "Заказать" в середине страницы
    def test_registration_scooter_order_middle(self, driver, name, last_name, street, subway, phone):
        rent_scooter_page = RegistrationPageScooter(driver)
        # кликнуть на кнопку да все привыкли
        rent_scooter_page.click_cookie()
        # заполняю поля формы страницы заказа
        rent_scooter_page.create_order(name, last_name, street, subway, phone, rent_scooter_page.order_middle)
        # заполняю поля формы страницы аренды
        rent_scooter_page.create_rent()
