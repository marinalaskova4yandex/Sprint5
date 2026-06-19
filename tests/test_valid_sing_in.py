import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators

def test_user_authorization(driver, authorized_user):
    # Проверяем, что мы на главной странице
    WebDriverWait(driver, 30).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/")
    )

    # Проверяем, что на экране появилась кнопка авторизованного пользователя
    order_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )

    # Обязательная проверка assert для фреймворка pytest
    assert order_button.is_displayed(), "Ошибка: Кнопка 'Оформить заказ' не отображается!"
    print("Успешная авторизация с корректным логином и паролем.")
    time.sleep(3)