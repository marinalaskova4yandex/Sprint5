from selenium.webdriver.common.by import By

class BaseInputLocators:
    """Общие локаторы полей для разных страниц (чтобы избежать дублирования)"""
    # Поле ввода Email
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    
    # Поле ввода Пароля
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")


class RegisterPageLocators(BaseInputLocators):
    """Локаторы для страницы регистрации"""

    # Ссылка «Войти» внизу формы регистрации
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

    # Поле "Имя"
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Проверка появления ошибки регистрации 
    ERROR_MESSAGE = (By.XPATH, "//*[text()='Некорректный пароль']")


class LoginPageLocators(BaseInputLocators):
    """Локаторы для страницы авторизации"""

    # Кнопка «Войти»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


class MainPageLocators:
    """Локаторы для Главной страницы (Конструктора)"""

    # Кнопка «Оформить заказ» (появляется у авторизованного пользователя)
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Вкладка «Начинки» 
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

    # Вкладка «Булки»
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")

    # Вкладка «Соусы»
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")

    # Логотип Stellar Burgers в шапке сайта 
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a") 

    # Главный заголовок Конструктора "Соберите бургер"
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")

    # Кнопка «Конструктор» в шапке сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")

    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")


class ProfilePageLocators:
    """Локаторы для страницы профиля (Личного кабинета)"""

    # Кнопка «Личный кабинет» на главной странице (в шапке сайта)
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")

    # Поле 'Имя' внутри личного кабинета
    NAME_PROFILE_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    # Кнопка «Выход» в меню личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class ForgotPasswordPageLocators:
    """Локаторы для страницы восстановления пароля"""

    # Ссылка «Войти» внизу формы восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")