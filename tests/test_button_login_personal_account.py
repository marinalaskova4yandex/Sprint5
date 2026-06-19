import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import ProfilePageLocators, LoginPageLocators, MainPageLocators

# Передаём фикстуры driver и registered_user из conftest.py
def test_login_via_personal_profile_button(driver, registered_user):
    # Данные пользователя теперь автоматически берутся из фикстуры registered_user
    test_email = registered_user["email"]
    test_password = registered_user["password"]

    # Очищаем cookies для имитации неавторизованного пользователя
    driver.delete_all_cookies()
    driver.get("https://stellarburgers.education-services.ru/")

    # Находим кнопку «Личный кабинет» в шапке сайта и кликаем по ней
    profile_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(ProfilePageLocators.PROFILE_BUTTON)
    )
    profile_button.click()

    # Проверяем, что после клика нас перенаправило на страницу входа (/login)
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/login")
    )

    # Заполняем форму авторизации
    login_email_input = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    login_email_input.send_keys(test_email)

    login_password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    login_password_input.send_keys(test_password)

    # Нажимаем кнопку «Войти»
    login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    login_button.click()

    # После входа сайт должен вернуть нас обратно на главную страницу
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/")
    )

    # Проверяем появление кнопки «Оформить заказ»
    order_button = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )

    # Итоговая проверка для pytest
    assert order_button.is_displayed(), "Ошибка: кнопка 'Оформить заказ' не появилась на экране"
    print("Выполнен вход через кнопку «Личный кабинет».")

    # Пауза перед тем, как фикстура driver закроет браузер
    time.sleep(5)