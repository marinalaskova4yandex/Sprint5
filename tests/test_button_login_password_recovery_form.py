import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Импортируем локаторы
from locators import ForgotPasswordPageLocators, LoginPageLocators, MainPageLocators

# Передаем фикстуры driver и registered_user из conftest.py
def test_login_via_link_in_forgot_password_form(driver, registered_user):
        
    # Данные пользователя теперь автоматически берутся из фиктуры registered_user
    test_email = registered_user["email"]
    test_password = registered_user["password"]
            
    #Переход на страницу восстановления пароля
    driver.get("https://stellarburgers.education-services.ru/forgot-password")

    # Находим стег <a> с текстом 'Войти' внизу формы восстановления пароля и кликаем по ней
    login_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)
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

    # Нажимаем большую кнопку "Войти"
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
    print("Прозведён вход через кнопку в форме восстановления пароля.")
    
    # Небольшая пауза перед автоматическим закрытием браузера фикстурой
    time.sleep(5)