import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.login_page import RegistrationPageScooter


class TestRegistrationPageScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Mozilla
        cls.driver = webdriver.Firefox()
        # перешли на страницу
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        # создадим объект класса страницы
        cls.rent_scooter_page = RegistrationPageScooter(cls.driver)

    @allure.title('Заказать самокат через кнопку "Заказать" вверху страницы')
    @allure.description("Заполнить форму заказа и проверить что появилось всплывающее окно с сообщение об успешном создании заказа")
    # Заказать самокат через кнопку "Заказать" вверху страницы
    def test_registration_scooter_order_up(self):
        # кликнуть на кнопку да все привыкли
        self.rent_scooter_page.click_cookie()
        # заполняю поля формы страницы заказа
        self.rent_scooter_page.create_order("Екатерина", "Никитина", "Пятницкая", "Пражская", "+79999999999")
        # заполняю поля формы страницы аренды
        self.rent_scooter_page.create_rent()

    @allure.title('Заказать самокат через кнопку "Заказать" в середине страницы')
    @allure.description("Заполнить форму заказа и проверить что появилось всплывающее окно с сообщение об успешном создании заказа")
    # Заказать самокат через кнопку "Заказать" в середине страницы
    def test_registration_scooter_order_middle(self):
        # заполняю поля формы страницы заказа
        self.rent_scooter_page.create_order("Иван", "Иванов", "Треугольная", "Южная", "+78888888888")
        # заполняю поля формы страницы аренды
        self.rent_scooter_page.create_rent()

    @classmethod
    def teardown_class(cls):
        # закроем браузер
        cls.driver.quit()
