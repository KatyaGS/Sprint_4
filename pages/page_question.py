from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class PageQuestion:
    # опишем элементы на странице раздела "Вопросы о важном"
    # поле "вопросы о важном"
    question_about_important = [By.XPATH, '//*[contains(@class, "Home_FourPart")]//*[contains (text(), "Вопросы о важном")]']
    # принять куки
    accept_cookies = [By.XPATH, '//*[@id="rcc-confirm-button"]']
    # Сколько это стоит? И как оплатить?
    how_much_cost = [
        By.XPATH,
        '//*[@id="accordion__heading-0"]',
    ]
    # Хочу сразу несколько самокатов! Так можно?
    several_scooters = [By.XPATH, '//*[@id="accordion__heading-1"]']
    # Как рассчитывается время аренды?
    rental_time = [By.XPATH, '//*[@id="accordion__heading-2"]']
    # Можно ли заказать самокат прямо на сегодня?
    order_scooter_today = [By.XPATH, '//*[@id="accordion__heading-3"]']
    # Можно ли продлить заказ или вернуть самокат раньше?
    extend_return_scooter = [By.XPATH, '//*[@id="accordion__heading-4"]']
    # Вы привозите зарядку вместе с самокатом?
    chargers_with_scooter = [By.XPATH, '//*[@id="accordion__heading-5"]']
    # Можно ли отменить заказ?
    cancel_order = [By.XPATH, '//*[@id="accordion__heading-6"]']
    # Я жизу за МКАДом, привезёте?
    live_outside_mkad = [By.XPATH, '//*[@id="accordion__heading-7"]']

    # текст ответа на вопрос "Сколько это стоит? И как оплатить?"
    how_much_cost_answer = [
        By.XPATH,
        '//*[@id="accordion__panel-0"]/p',
    ]
    # текст ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"
    several_scooters_answer = [
        By.XPATH,
        '//*[@id="accordion__panel-1"]/p',
    ]
    # текст ответа на вопрос "Как рассчитывается время аренды?"
    rental_time_answer = [
        By.XPATH,
        '//*[@id="accordion__panel-2"]/p',
    ]
    # текст ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"
    order_scooter_today_answer = [
        By.XPATH,
        '//*[@id="accordion__panel-3"]/p',
    ]
    # текст ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    extend_return_scooter_answer = [
        By.XPATH,
        '//*[@id="accordion__panel-4"]/p',
    ]
    # текст ответа на вопрос "Вы привозите зарядку вместе с самокатом?"
    chargers_with_scooter_answer = [
        By.XPATH,
        '//*[@id="accordion__panel-5"]/p',
    ]
    # текст ответа на вопрос "Можно ли отменить заказ?"
    cancel_order_answer = [
        By.XPATH,
        '//*[@id="accordion__panel-6"]/p',
    ]
    # текст ответа на вопрос "Я жизу за МКАДом, привезёте?"
    live_outside_mkad_answer = [
        By.XPATH,
        '//*[@id="accordion__panel-7"]/p',
    ]

    # текста ответов на вопросы
    how_much_cost_answer_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    several_scooters_answer_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    rental_time_answer_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    order_scooter_today_answer_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    extend_return_scooter_answer_text = (
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    )
    chargers_with_scooter_answer_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    cancel_order_answer_text = (
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    )
    live_outside_mkad_answer_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    # конструктор класса (смогу задать любой драйвер)
    def __init__(self, driver):
        self.driver = driver

    # кликаем на куки
    def click_on_cookies(self):
        self.driver.find_element(*self.accept_cookies).click()

    # метод кликает на стрелочку
    def click(self, xpath):
        self.driver.find_element(*xpath).click()

    # метод проверяет наличие атрибута "aria-expanded" у элемента
    def check_attribute(self, xpath):
        return self.driver.find_element(*xpath).get_attribute("aria-expanded")

    # получить текст ответа
    def get_answer_text(self, xpath):
        return self.driver.find_element(*xpath).text

    # метод ожидания загрузки страницы
    def wait_for_load(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.question_about_important))

    # дожидаемся загрузки страницы и принимаем куки
    def load_page(self):
        self.wait_for_load()
        self.click_on_cookies()
