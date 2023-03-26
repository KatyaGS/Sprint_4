from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class RegistrationPageScooter:
    # локатор кнопки "Заказать" вверху стр
    order_up = [By.XPATH, "/html/body/div/div/div[1]/div[1]/div[2]/button[1]"]
    # локатор кнопки "Заказать" в середине стр
    order_middle = [By.XPATH, "/html/body/div/div/div[1]/div[4]/div[2]/div[5]/button"]
    # локатор поля "Имя"
    first_name = [By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/input"]
    # локатор поля "Фамилия"
    last_name = [By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/input"]
    # локатор поля "Адрес: куда привезти заказ"
    address = [By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]/input"]
    # локатор поля "Станция метро"
    subway = [By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div/div/input"]
    # локатор поля "Телефон: на него позвонит курьер"
    mobile_phone = [By.XPATH, "/html/body/div/div/div[2]/div[2]/div[5]/input"]
    # локатор кнопки "Далее" (на стр "Для кого самокат")
    forward_button = [By.XPATH, "/html/body/div/div/div[2]/div[3]/button"]
    # локатор первого элемента в выпадающем списке станции метро (на стр "Для кого самокат")
    subway_menu_element = [
        By.XPATH,
        "/html/body/div/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[1]/button",
    ]
    # локатор для кнопки подтверждения использования cookie
    cookie = [By.XPATH, '//*[@id="rcc-confirm-button"]']
    # локатор для поля "Когда привезти самокат" (на стр "Про аренду")
    data_rent = [By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div/input"]
    # локатор стрелочки вперед в календаре
    data_rent_next_month = [
        By.XPATH,
        "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/button[2]",
    ]
    # локатор даты
    data_rent_day = [
        By.XPATH,
        "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[6]",
    ]
    # локатор для поля "Срок аренды"
    period_rent = [By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]"]
    # локатор срока на четверо суток
    period_rent_menu_element = [
        By.XPATH,
        "/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[4]",
    ]
    # локатор для поля "Цвет самоката" (цвет:черный жемчуг)
    color_scooter_black = [By.XPATH, '//*[@id="black"]']
    # локатор для поля "Цвет самоката" (цвет:серая безысходность)
    color_scooter_grey = [By.XPATH, '//*[@id="black"]']
    # локатор для поля "Комментарий для курьера"
    comments = [By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/input"]
    # локатор для кнопки "Заказать" (на стр "Про аренду")
    order_button = [By.XPATH, "/html/body/div/div/div[2]/div[3]/button[2]"]
    # локатор для кнопки "Назад" (на стр "Про аренду")
    back_button = [By.XPATH, "/html/body/div/div/div[2]/div[3]/button[1]"]
    # локатор всплывающего окошка с кнопкой "Да"
    pop_up_window_yes = [By.XPATH, "/html/body/div/div/div[2]/div[5]/div[2]/button[2]"]
    # локатор всплывающего окошка с кнопкой "Нет"
    pop_up_window_no = [By.XPATH, "/html/body/div/div/div[2]/div[5]/div[2]/button[1]"]
    # локатор текста в сплывающем окошке "Заказ оформлен"
    order_processed = [By.XPATH, "/html/body/div/div/div[2]/div[5]/div[1]"]
    # локатор кнопки "Посмотреть статус"
    status = [By.XPATH, "/html/body/div/div/div[2]/div[5]/div[2]/button"]
    # локатор логотипа "Самокат"
    logo_scooter = [By.XPATH, "/html/body/div/div/div[1]/div[1]/a[2]/img"]

    # конструктор класса (смогу задать любой драйвер)
    def __init__(self, driver):
        self.driver = driver

    # метод заполняет поле "Имя"
    def set_first_name(self, test_name):
        self.driver.find_element(*self.first_name).send_keys(test_name)

    # метод заполняет поле "Фамилия"
    def set_last_name(self, test_last_name):
        self.driver.find_element(*self.last_name).send_keys(test_last_name)

    # метод заполняет поле "Адрес: куда привезти заказ"
    def set_address(self, test_address):
        self.driver.find_element(*self.address).send_keys(test_address)

    # метод заполняет поле "Станция метро"
    # сначала найти поле
    def set_subway(self, test_subway):
        self.driver.find_element(*self.subway).send_keys(test_subway)

    def select_subway(self):
        self.driver.find_element(*self.subway_menu_element).click()

    # метод заполняет поле "Телефон: на него позвонит курьер"
    def set_mobile_phone(self, test_mobile_phone):
        self.driver.find_element(*self.mobile_phone).send_keys(test_mobile_phone)

    # метод проверяет активна ли кнопка "Заказать" вверху стр
    def click_order_up(self):
        self.driver.find_element(*self.order_up).click()

    # метод проверяет активна ли кнопка "Заказать" внизу стр
    def click_order_middle(self):
        self.driver.find_element(*self.order_middle).click()

    # метод проверяет активна ли кнопка "Далее" (после ввода данных в регистрации, на стр "Для кого самокат")
    def click_forward_button(self):
        self.driver.find_element(*self.forward_button).click()

    # метод  нажимает на кнопку cookie "да все привыкли"
    def click_cookie(self):
        self.driver.find_element(*self.cookie).click()

    # метод заполняет поле "Когда привезти самокат"
    # сначала найти поле
    def set_data_rent(self):
        self.driver.find_element(*self.data_rent).click()

    def select_data_rent_next_month(self):
        self.driver.find_element(*self.data_rent_next_month).click()

    def select_data_rent_day(self):
        self.driver.find_element(*self.data_rent_day).click()

    # метод заполняет поле "Срок аренды"
    def set_period_rent(self):
        self.driver.find_element(*self.period_rent).click()

    def select_period_rent(self):
        self.driver.find_element(*self.period_rent_menu_element).click()

    # метод заполняет поле "Цвет самоката"
    def set_color_scooter_black(self):
        self.driver.find_element(*self.color_scooter_black).click()

    # метод заполняет поле "Комментарий для курьера"
    def set_comments(self):
        self.driver.find_element(*self.comments).send_keys("Не опаздывайте, пожалуйста")

    # метод нажимает на кнопку "Заказать" (на стр Про аренду)
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    # метод нажимает на кнопку "Да" (в сплывающем окне "Хотите оформить заказ?")
    def click_pop_up_window_yes(self):
        self.driver.find_element(*self.pop_up_window_yes).click()

    # метод для текста "Заказ оформлен"
    def get_order_processed(self):
        return self.driver.find_element(*self.order_processed).text

    # метод нажимает на кнопку "Посмотреть статус"
    def click_status(self):
        self.driver.find_element(*self.status).click()

    # метод нажимает на логотип "Самокат"
    def click_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()

    # метод ожидания загрузки страницы
    def wait_for_load_registration_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_up))

    # метод для проверки оформления заказа
    def check_order(self):
        # новой переменной присваивается значение текста элемента оформленного заказа
        result = self.get_order_processed()
        # проверяется что есть надпись "Заказ оформлен" в переменной
        assert "Заказ оформлен" in result

    # объединить методы для заполнения страницы "Для кого самокат"
    def create_order(self, test_name, test_last_name, test_address, test_subway, test_mobile_phone):
        # дождёмся загрузки страницы
        self.wait_for_load_registration_page()
        # кликнуть на кнопку "Заказать"
        self.click_order_up()
        # ввести имя
        self.set_first_name(test_name)
        # ввести фамилию
        self.set_last_name(test_last_name)
        # ввести адрес
        self.set_address(test_address)
        # выбрать окно для ввода станция метро
        self.set_subway(test_subway)
        # выбрать первый элемент из выпадающего списка
        self.select_subway()
        # ввести номер телефона
        self.set_mobile_phone(test_mobile_phone)
        # кликнуть на кнопку "Далее"
        self.click_forward_button()

    # объединить методы для заполнения страницы "Про аренду"
    def create_rent(self):
        # выбрать окно для выбора "Срока аренды"
        self.set_period_rent()
        # выбрать элемент из выпадающего списка
        self.select_period_rent()
        # в пол "Цвет самоката" выбрать цвет "черный жемчуг"
        self.set_color_scooter_black()
        # ввести комментарий для курьера
        self.set_comments()
        # кликнуть на поле с календарем
        self.set_data_rent()
        # выбрать дату в календаре (следующий месяц)
        self.select_data_rent_next_month()
        # выбрать дату в календаре (день)
        self.select_data_rent_day()
        # кликнуть на кнопку "Заказать" (на стр Про аренду)
        self.click_order_button()
        # кликнуть на кнопку "Да" в сплывающем окне "Хотите оформить заказ?"
        self.click_pop_up_window_yes()
        # проверка что заказ оформился
        self.check_order()
        # кликнуть на кнопку "Посмотреть статус"
        self.click_status()
        # кликнуть на лого "Самокат"
        self.click_logo_scooter()
