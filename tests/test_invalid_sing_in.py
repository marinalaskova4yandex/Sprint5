#Тест регистрации. Ошибка для некорректного пароля.
import logging
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Импортируем функции generate_fake_email, generate_fake_password
from random_login_password import generate_fake_email, generate_fake_password

#  Загружаем классы локаторов из файла locators.py
from locators import RegisterPageLocators

class TestRegistrationMainPage:

    # Передаем в аргумент self и фикстуру driver из conftest.py
    def test_registration_with_short_password(self, driver):
        fake = Faker()

        test_name = fake.first_name()
        test_email = generate_fake_email()
        # Берем первые 5 символов для негативного теста
        short_password = generate_fake_password(6)[:5]

        # регистрация пользователя (используем driver из фикстуры)
        driver.get("https://stellarburgers.education-services.ru/register")

        # Заполняем поле "Имя"
        name_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
        )
        name_input.send_keys(test_name)

        # Заполняем поле "Email"
        reg_email_input = driver.find_element(*RegisterPageLocators.EMAIL_INPUT)
        reg_email_input.send_keys(test_email)

        # Заполняем поле "Пароль"
        reg_password_input = driver.find_element(*RegisterPageLocators.PASSWORD_INPUT)
        reg_password_input.send_keys(short_password)

        # Нажимаем кнопку "Зарегистрироваться"
        register_button = driver.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        register_button.click()

        # проверка появления ошибки регистрации 
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE)
        )        
        logging.info(f"Обнаружена ошибка: '{error_message.text}'")

        # Проверяем, что мы остались на странице регистрации
        assert (
            driver.current_url
            == "https://stellarburgers.education-services.ru/register"
        )
        
        # Логируем успешное действие 
        logging.info("Выполняем проверку что пользователь остался на странице регистрации")
        assert True
        logging.info("Проверка URL пройдена: пользователь остался на странице регистрации.")