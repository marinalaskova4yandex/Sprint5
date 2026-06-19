import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Загружаем классы локаторов из файла locators.py
from locators import LoginPageLocators, MainPageLocators

# Передаем в аргументы фикстуры driver и registered_user из conftest.py
def test_user_authorization(driver, registered_user):
    
    
    # Добавляем email и пароль, которые сгенерировала и зарегистрировала фикстура
    test_email = registered_user["email"]
    test_password = registered_user["password"]
       
    # Авторизация (вход)
    # можно явно открыть страницу авторизации
    driver.get("https://stellarburgers.education-services.ru/login")

    # Находим и заполняем поле Email для входа
    login_email_input = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    login_email_input.send_keys(test_email)

    # Находим и заполняем поле Пароль для входа
    login_password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    login_password_input.send_keys(test_password)

    # Нажимаем кнопку "Войти"
    login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    login_button.click()


    # проверка успешного входа
    # Проверяем, что URL изменился на главную страницу
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/")
    )

    # Проверяем, что на экране появилась кнопка авторизованного пользователя
    order_button = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )
    
    # Обязательная проверка assert для фреймворка pytest
    assert order_button.is_displayed(), "Ошибка: Кнопка 'Оформить заказ' не отображается!"
    print("Успешная регистрация с корректным логином и паролем.")

    # Небольшая пауза, после чего фикстура driver автоматически закроет браузер
    time.sleep(5)