#Тест вход через кнопку в форме регистрации
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import RegisterPageLocators, LoginPageLocators, MainPageLocators

class TestAuthorization:

    # Передаём фикстуры driver и registered_user из conftest.py, добавляя self
    def test_login_via_link_in_register_form(self, driver, registered_user):
        # Добавляем email и пароль, которые сгенерировала и зарегистрировала фикстура
        test_email = registered_user["email"]
        test_password = registered_user["password"]
      
        # Переход на страницу регистрации
        driver.get("https://stellarburgers.education-services.ru/register")
        
        # Находим тег <a> с текстом 'Войти' внизу формы регистрации и кликаем по ней
        login_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)
        )
        login_link.click()
        
        # Проверяем, что после клика по ссылке нас перенаправило на страницу входа (/login)
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

        # Нажимаем большую кнопку «Войти»
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
        

        # Логируем успешное действие 
        logging.info("Выполняем переход через кнопку в форме регистрации")
        assert True
        logging.info("Успешно выполнен вход через кнопку в форме регистрации.")