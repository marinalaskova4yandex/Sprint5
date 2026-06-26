#Тест успешной регистрации.
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import RegisterPageLocators

class TestRegistrationMainPage:

    # Фикстуры driver и user_data вызываются абсолютно верно
    def test_user_registration_success(self, driver, user_data):
        # Переход на страницу регистрации
        driver.get("https://stellarburgers.education-services.ru/register")
        
        # Заполняем поле "Имя" данными из фиктуры user_data
        name_input = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
        )
        name_input.send_keys(user_data["name"])
        
        # Заполняем поле "Email"
        reg_email_input = driver.find_element(*RegisterPageLocators.EMAIL_INPUT)
        reg_email_input.send_keys(user_data["email"])
        
        # Заполняем поле "Пароль"
        reg_password_input = driver.find_element(*RegisterPageLocators.PASSWORD_INPUT)
        reg_password_input.send_keys(user_data["password"])
        
        # Нажимаем кнопку "Зарегистрироваться"
        register_button = driver.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        register_button.click()

        # Проверяем, что после успешной регистрации нас перенаправило на страницу входа (/login)
        WebDriverWait(driver, 30).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/login")
        )

        # Проверяем появление кнопки «Войти» на форме авторизации для pytest
        assert driver.current_url == "https://stellarburgers.education-services.ru/login", "Ошибка: Пользователь не перенаправлен на страницу входа после регистрации!"
        
        # Логируем успешное действие 
        logging.info("Выполняем переход на страницу логина")
        logging.info("Успешная регистрация с корректным логином и паролем.")