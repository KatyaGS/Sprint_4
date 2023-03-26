import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.page_question import PageQuestion


class TestPageQuestion:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Mozilla
        cls.driver = webdriver.Firefox()

        # перешли на страницу
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        # создадим объект класса страницы
        cls.questions = PageQuestion(cls.driver)
        cls.driver.maximize_window()

    @allure.title("Тест кнопки принятия cookies")
    @allure.description('На главной странице нажать на кнопку "да все  привыкли"')
    # ожидаем загрузки страницы и кликаем на куки
    def test_accept_cookies(self):
        self.questions.load_page()

    @allure.title('Проверка поля "Сколько это стоит? И как оплатить?"')  # декоратор
    @allure.description(
        "На странице ищем элемент, кликаем на стрелочку и проверяем что он раскрылся и проверяем правильный ли у него текст"
    )
    # проверяем "Сколько это стоит? И как оплатить?"
    def test_question_how_much_cost(self):
        # кликаем на стрелочку
        self.questions.click(self.questions.how_much_cost)
        # проверяем, что атрибут "aria-expanded" стал равен "true" после нажатия
        assert self.questions.check_attribute(self.questions.how_much_cost) == "true"
        # Проверяем текст ответа
        assert self.questions.get_answer_text(self.questions.how_much_cost_answer) == self.questions.how_much_cost_answer_text

    @allure.title('Проверка поля "Хочу сразу несколько самокатов! Так можно?"')  # декоратор
    @allure.description(
        "На странице ищем элемент, кликаем на стрелочку и проверяем что он раскрылся и проверяем правильный ли у него текст"
    )
    # проверяем "Хочу сразу несколько самокатов! Так можно?"
    def test_question_several_scooters(self):
        # кликаем на стрелочку
        self.questions.click(self.questions.several_scooters)
        # проверяем, что атрибут "aria-expanded" стал равен "true" после нажатия
        assert self.questions.check_attribute(self.questions.several_scooters) == "true"
        # Проверяем текст ответа
        assert self.questions.get_answer_text(self.questions.several_scooters_answer) == self.questions.several_scooters_answer_text

    @allure.title('Проверка поля "Как рассчитывается время аренды?"')  # декоратор
    @allure.description(
        "На странице ищем элемент, кликаем на стрелочку и проверяем что он раскрылся и проверяем правильный ли у него текст"
    )
    # проверяем "Как рассчитывается время аренды?"
    def test_question_rental_time(self):
        # кликаем на стрелочку
        self.questions.click(self.questions.rental_time)
        # проверяем, что атрибут "aria-expanded" стал равен "true" после нажатия
        assert self.questions.check_attribute(self.questions.rental_time) == "true"
        # Проверяем текст ответа
        assert self.questions.get_answer_text(self.questions.rental_time_answer) == self.questions.rental_time_answer_text

    @allure.title('Проверка поля "Можно ли заказать самокат прямо на сегодня?"')  # декоратор
    @allure.description(
        "На странице ищем элемент, кликаем на стрелочку и проверяем что он раскрылся и проверяем правильный ли у него текст"
    )
    # проверяем "Можно ли заказать самокат прямо на сегодня?"
    def test_question_order_scooter_today(self):
        # кликаем на стрелочку
        self.questions.click(self.questions.order_scooter_today)
        # проверяем, что атрибут "aria-expanded" стал равен "true" после нажатия
        assert self.questions.check_attribute(self.questions.order_scooter_today) == "true"
        # Проверяем текст ответа
        assert self.questions.get_answer_text(self.questions.order_scooter_today_answer) == self.questions.order_scooter_today_answer_text

    @allure.title('Проверка поля "Можно ли продлить заказ или вернуть самокат раньше?"')  # декоратор
    @allure.description(
        "На странице ищем элемент, кликаем на стрелочку и проверяем что он раскрылся и проверяем правильный ли у него текст"
    )
    # проверяем "Можно ли продлить заказ или вернуть самокат раньше?"
    def test_question_extend_return_scooter(self):
        # кликаем на стрелочку
        self.questions.click(self.questions.extend_return_scooter)
        # проверяем, что атрибут "aria-expanded" стал равен "true" после нажатия
        assert self.questions.check_attribute(self.questions.extend_return_scooter) == "true"
        # Проверяем текст ответа
        assert (
            self.questions.get_answer_text(self.questions.extend_return_scooter_answer) == self.questions.extend_return_scooter_answer_text
        )

    @allure.title('Проверка поля "Вы привозите зарядку вместе с самокатом?"')  # декоратор
    @allure.description(
        "На странице ищем элемент, кликаем на стрелочку и проверяем что он раскрылся и проверяем правильный ли у него текст"
    )
    # проверяем "Вы привозите зарядку вместе с самокатом?"
    def test_question_chargers_with_scooter(self):
        # кликаем на стрелочку
        self.questions.click(self.questions.chargers_with_scooter)
        # проверяем, что атрибут "aria-expanded" стал равен "true" после нажатия
        assert self.questions.check_attribute(self.questions.chargers_with_scooter) == "true"
        # Проверяем текст ответа
        assert (
            self.questions.get_answer_text(self.questions.chargers_with_scooter_answer) == self.questions.chargers_with_scooter_answer_text
        )

    @allure.title('Проверка поля "Можно ли отменить заказ?"')  # декоратор
    @allure.description(
        "На странице ищем элемент, кликаем на стрелочку и проверяем что он раскрылся и проверяем правильный ли у него текст"
    )
    # проверяем "Можно ли отменить заказ?"
    def test_question_cancel_order(self):
        # кликаем на стрелочку
        self.questions.click(self.questions.cancel_order)
        # проверяем, что атрибут "aria-expanded" стал равен "true" после нажатия
        assert self.questions.check_attribute(self.questions.cancel_order) == "true"
        # Проверяем текст ответа
        assert self.questions.get_answer_text(self.questions.cancel_order_answer) == self.questions.cancel_order_answer_text

    @allure.title('Проверка поля "Я жизу за МКАДом, привезёте?"')  # декоратор
    @allure.description(
        "На странице ищем элемент, кликаем на стрелочку и проверяем что он раскрылся и проверяем правильный ли у него текст"
    )
    # проверяем "Я жизу за МКАДом, привезёте?"
    def test_question_live_outside_mkad(self):
        # кликаем на стрелочку
        self.questions.click(self.questions.live_outside_mkad)
        # проверяем, что атрибут "aria-expanded" стал равен "true" после нажатия
        assert self.questions.check_attribute(self.questions.live_outside_mkad) == "true"
        # Проверяем текст ответа
        assert self.questions.get_answer_text(self.questions.live_outside_mkad_answer) == self.questions.live_outside_mkad_answer_text

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
