# Тест что работают переходы к разделу «Булки»
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Загружаем классы локаторов из файла locators.py
from locators import MainPageLocators

# URL главной страницы с конструктором
URL_MAIN = "https://stellarburgers.education-services.ru/"

class TestNavigation:

    # Передаем в аргумент self и фиктуру driver из conftest.py
    def test_constructor_tab_buns(self, driver):
        driver.get(URL_MAIN)
        
        # Находим вкладки «Булки» и «Соусы»
        bun_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)
        )
        sauce_tab = driver.find_element(*MainPageLocators.SAUCES_TAB)
        
        # Так как «Булки» активны сразу, сначала кликаем на «Соусы», чтобы сменить фокус
        sauce_tab.click()
        
        
        # Теперь кликаем обратно на «Булки»
        bun_tab.click()
        
        # Проверяем, что вкладка «Булки» снова стала активной
        assert "tab_tab_type_current" in bun_tab.get_attribute("class"), (
            "Ошибка: Вкладка 'Булки' не вернула фокус!"
        )
        
        # Логируем успешное действие 
        logging.info("Выполняем переход к разделу «Булки»")
        assert True
        logging.info("Переход к разделу «Булки» выполнен.")