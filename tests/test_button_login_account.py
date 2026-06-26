# Вход по кнопке «Войти в аккаунт» на главной странице
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Импортируем локаторы
from locators import MainPageLocators, LoginPageLocators

class TestAuthorization:

    # Передаем в аргументы self, а также фикстуры driver и registered_user из conftest.py
    def test_login_via_main_page_button(self, driver, registered_user):
            
        # Данные пользователя теперь автоматически берутся из фиктуры registered_user
        test_email = registered_user["email"]
        test_password = registered_user["password"]
        
        # переход на главную страницу и клик по кнопке войти в аккаунт
        driver.get("https://stellarburgers.education-services.ru/")

        # Находим кнопку «Войти в аккаунт» на главной странице и кликаем
        login_account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON)
        )
        login_account_button.click()
        
        
        # Проверяем, что после клика нас перенаправило на страницу входа
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

        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        
        # После входа сайт должен вернуть нас обратно на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        

        # появление кнопки «Оформить заказ» вместо «Войти в аккаунт»
        order_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        # Финальная проверка assert — обязательна для тестов в pytest
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не появилась на экране"
        

        # Логируем успешное действие 
        logging.info("Выполняем переход по кнопке «Войти в аккаунт» на главной странице")
        assert True
        logging.info("Выполнен вход по кнопке «Войти в аккаунт» на главной странице.")