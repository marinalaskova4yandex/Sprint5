import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Импортируем локаторы
from locators import ProfilePageLocators, MainPageLocators

# Передаем в аргументы фикстуры driver и registered_user из conftest.py
def test_navigate_from_profile_to_constructor_via_button(driver, authorized_user):
    # С главной страницы переходим в Личный кабинет (чтобы было откуда возвращаться)
    profile_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(ProfilePageLocators.PROFILE_BUTTON)
    )
    profile_button.click()

    # Дождемся, что оказались в профиле
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/account/profile")
    )

    # Нажимаем на кнопку «Конструктор» в шапке сайта
    constructor_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
    )
    constructor_button.click()

    # Проверяем, что URL изменился на главную страницу
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/")
    )

    # Шаг 4: Проверяем наличие главного заголовка Конструктора
    constructor_header = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_HEADER)
    )

    assert constructor_header.is_displayed(), "Ошибка: Заголовок 'Соберите бургер' не найден!"
    print("Выполнен переход по клику на «Конструктор».")
    time.sleep(5)