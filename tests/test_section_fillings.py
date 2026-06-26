# Тест что работают переходы к разделу «Начинки»
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Загружаем классы локаторов из файла locators.py
from locators import MainPageLocators

# URL главной страницы с конструктором
URL_MAIN = "https://stellarburgers.education-services.ru/"

class TestNavigation:

    #  Передаем в аргумент self и фиктуру driver из conftest.py
    def test_constructor_tab_fillings(self, driver):
        driver.get(URL_MAIN)
        
        # Находим вкладку «Начинки» и кликаем по ней
        filling_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)
        )
        filling_tab.click()
        
        # Проверяем, что вкладка «Начинки» стала активной
        assert "tab_tab_type_current" in filling_tab.get_attribute("class"), (
            "Ошибка: Вкладка 'Начинки' не стала активной!"
        )
        
        # Логируем успешное действие 
        logging.info("Выполняем переход к разделу «Начинки»")
        assert True
        logging.info("Переход к разделу «Начинки» выполнен.")