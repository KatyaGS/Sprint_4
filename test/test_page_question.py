import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.page_question import PageQuestion
import pytest


class TestPageQuestion:
    # 1. кнопка со стрелочкой
    # 2. локатор атрибута aria-expanded
    # 3. сравнить текст который показывается при открытии стрелочки с текстом который у нас уже есть

    test_data_object = PageQuestion(None)
    test_data_how_much_cost = [
        test_data_object.how_much_cost,
        test_data_object.how_much_cost_answer,
        test_data_object.how_much_cost_answer_text,
    ]

    test_data_several_scooters = [
        test_data_object.several_scooters,
        test_data_object.several_scooters_answer,
        test_data_object.several_scooters_answer_text,
    ]

    test_data_rental_time = [
        test_data_object.rental_time,
        test_data_object.rental_time_answer,
        test_data_object.rental_time_answer_text,
    ]

    test_data_order_scooter_today = [
        test_data_object.order_scooter_today,
        test_data_object.order_scooter_today_answer,
        test_data_object.order_scooter_today_answer_text,
    ]

    test_data_extend_return_scooter = [
        test_data_object.extend_return_scooter,
        test_data_object.extend_return_scooter_answer,
        test_data_object.extend_return_scooter_answer_text,
    ]

    test_data_chargers_with_scooter = [
        test_data_object.chargers_with_scooter,
        test_data_object.chargers_with_scooter_answer,
        test_data_object.chargers_with_scooter_answer_text,
    ]

    test_data_cancel_order = [
        test_data_object.cancel_order,
        test_data_object.cancel_order_answer,
        test_data_object.cancel_order_answer_text,
    ]

    test_data_live_outside_mkad = [
        test_data_object.live_outside_mkad,
        test_data_object.live_outside_mkad_answer,
        test_data_object.live_outside_mkad_answer_text,
    ]

    test_data = [
        test_data_how_much_cost,
        test_data_several_scooters,
        test_data_rental_time,
        test_data_order_scooter_today,
        test_data_extend_return_scooter,
        test_data_chargers_with_scooter,
        test_data_cancel_order,
        test_data_live_outside_mkad,
    ]

    @allure.title("Проверка поля")
    @allure.description(
        "На странице ищем элемент, кликаем на стрелочку и проверяем что он раскрылся и проверяем правильный ли у него текст"
    )
    @pytest.mark.parametrize("locator,answer,answer_text", test_data)
    def test_question(self, driver, locator, answer, answer_text):
        questions = PageQuestion(driver)
        questions.load_page()
        # кликаем на стрелочку
        questions.click(locator)
        # проверяем, что атрибут "aria-expanded" стал равен "true" после нажатия
        assert questions.check_attribute(locator) == "true"
        # Проверяем текст ответа
        assert questions.get_answer_text(answer) == answer_text
