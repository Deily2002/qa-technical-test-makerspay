from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Selectores
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_container = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login_to_app(self, user, pwd):
        """Método para realizar el flujo de login completo"""
        if user:
            self.driver.find_element(*self.username_field).send_keys(user)
        if pwd:
            self.driver.find_element(*self.password_field).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_container).text