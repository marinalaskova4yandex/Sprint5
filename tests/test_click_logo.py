import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Импортируем локаторы
from locators import ProfilePageLocators, MainPageLocators


class TestNavigation:

    # Переход из личного кабинета на логотип Stellar Burgers
    # Передаем в аргументы фикстуры driver и authorized_user из conftest.py
    def test_navigate_from_profile_to_constructor_via_logo(
        self, driver, authorized_user
    ):
        # Переходим в Личный кабинет
        profile_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(ProfilePageLocators.PROFILE_BUTTON)
        )
        profile_button.click()

        WebDriverWait(driver, 5).until(
            EC.url_to_be(
                "https://stellarburgers.education-services.ru/account/profile"
            )
        )

        # Нажимаем на логотип Stellar Burgers в самом центре шапки
        logo_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO_BUTTON)
        )
        logo_button.click()

        # Проверяем, что URL изменился на главную страницу
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )

        # Проверяем наличие главного заголовка Конструктора
        constructor_header = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                MainPageLocators.CONSTRUCTOR_HEADER
            )
        )

        assert (
            constructor_header.is_displayed()
        ), "Ошибка: Заголовок 'Соберите бургер' не найден после клика на логотип!"

        # Логируем успешное действие
        logging.info("Выполняем переход по клику на логотип Stellar Burgers.")
        assert True
        logging.info("Выполнен переход по клику на логотип Stellar Burgers.")