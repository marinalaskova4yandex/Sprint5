# Тест что работают переходы к разделу «Соусы»
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Загружаем классы локаторов из файла locators.py
from locators import LoginPageLocators, MainPageLocators

class TestNavigation:

    # Передаем в аргументы self и фиктуру driver из conftest.py
    def test_constructor_tab_sauces(self, driver):
        
        # Переход на главную страницу с конструктором
        driver.get("https://stellarburgers.education-services.ru/")

        # Находим вкладку «Соусы» и кликаем по ней
        sauce_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        )
        sauce_tab.click()
        
        # Проверяем, что вкладка «Соусы» стала активной
        assert "tab_tab_type_current" in sauce_tab.get_attribute("class"), (
            "Ошибка: Вкладка 'Соусы' не стала активной!"
        )
        
        # Логируем успешное действие 
        logging.info("Выполняем переход к разделу «Соусы»")
        assert True
        logging.info("Переход к разделу «Соусы» выполнен.")