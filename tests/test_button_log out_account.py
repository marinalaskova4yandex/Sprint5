# Тест выход по кнопке «Выйти» в личном кабинете.
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Импортируем локаторы
from locators import ProfilePageLocators, LoginPageLocators

class TestLogout:

    # Передаем фикстуры driver и authorized_user из conftest.py в аргументы
    def test_user_logout_from_personal_profile(self, driver, authorized_user):
        
        # Переход в Личный кабинет
        profile_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(ProfilePageLocators.PROFILE_BUTTON)
        )
        profile_button.click()
        
        # Дожидаемся загрузки страницы профиля
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/account/profile")
        )
        
        # Находим кнопку «Выход» в меню личного кабинета и кликаем по ней
        logout_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()
        

        # После выхода сайт должен мгновенно перенаправить на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/login")
        )
       
        # Финальная проверка: кнопка «Войти» на форме авторизации видна пользователю
        login_form_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        
        assert login_form_button.is_displayed(), "Ошибка: Кнопка 'Войти' не появилась на форме после выхода!"
        

        # Логируем успешное действие 
        logging.info("Выполняем переход по кнопке «Выйти» в личном кабинете")
        assert True
        logging.info("Выполнен выход по кнопке «Выйти» в личном кабинете.")