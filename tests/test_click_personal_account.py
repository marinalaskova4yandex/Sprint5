import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Импортируем локаторы
from locators import ProfilePageLocators

# Передаем в аргументы фикстуры driver и authorized_user из conftest.py
def test_go_to_personal_profile_page(driver, authorized_user):
    test_name = authorized_user["name"]

    # Находим кнопку «Личный кабинет» и кликаем по ней, браузер уже авторизован и стоит на главной странице
    profile_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(ProfilePageLocators.PROFILE_BUTTON)
    )
    profile_button.click()

    # Проверяем, что URL изменился на страницу профиля
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/account/profile")
    )

    # Проверим, что значение внутри поля 'Имя' совпадает с именем пользователя
    name_profile_input = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ProfilePageLocators.NAME_PROFILE_INPUT)
    )

    # Получаем текст, который отображается внутри поля ввода на сайте
    actual_name = name_profile_input.get_attribute("value")

    # Проверка через assert для pytest
    assert actual_name == test_name, f"Ошибка: Ожидалось имя {test_name}, но на странице отображается {actual_name}"
    print(f"Выполнен переход в личный кабинет по клику на «Личный кабинет».")

    time.sleep(5)