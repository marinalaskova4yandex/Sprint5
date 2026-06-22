import logging
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Инициализируем генератор случайных данных
fake = Faker()


# Автоматическая настройка логера (вывод в консоль и запись в файл automation.log)
@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler("automation.log", mode="w", encoding="utf-8"),
            logging.StreamHandler()  # Дублирование логов в консоль
        ]
    )


# 1. Фикстура для запуска и закрытия браузера
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    
    # Код ниже выполняется ПОСЛЕ каждого теста для обеспечения изолированности сессий
    try:
        browser.delete_all_cookies()  # Полная очистка куки-файлов
        browser.execute_script("window.localStorage.clear();")  # Очистка LocalStorage
        browser.execute_script("window.sessionStorage.clear();")  # Очистка SessionStorage
    except Exception as e:
        logging.warning(f"[Фикстура] Предупреждение при очистке куков/хранилища: {e}")
        
    browser.quit()


# 2. Фикстура генерации случайных данных
@pytest.fixture
def user_data():
    username = fake.user_name()
    email = f"{username}@yandex.ru"
    password = fake.password(length=8)
    name = fake.first_name()
    return {"name": name, "email": email, "password": password}


# 3. Фикстура, которая регистрирует пользователя на сайте
@pytest.fixture
def registered_user(driver, user_data):
    driver.get("https://stellarburgers.education-services.ru/register")
    
    name_input = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))
    )
    name_input.send_keys(user_data["name"])
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(user_data["email"])
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(user_data["password"])
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/login")
    )
    return user_data


# 4. Фикстура, которая выполняет полноценный вход
@pytest.fixture
def authorized_user(driver, registered_user):
    logging.info(f"[Фикстура] Авторизуем пользователя: {registered_user['email']}")
    
    driver.get("https://stellarburgers.education-services.ru/login")
    
    login_email_input = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
    )
    login_email_input.send_keys(registered_user["email"])
    
    login_password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    login_password_input.send_keys(registered_user["password"])
    
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/")
    )
    return registered_user