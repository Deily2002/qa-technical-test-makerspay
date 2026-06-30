import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage

def test_saucedemo_smoke():
    # Setup del navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    login = LoginPage(driver)
    
    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        # Escenario 1: Password incorrecto
        login.login_to_app("standard_user", "wrong_password")
        time.sleep(2)
        assert "Username and password do not match" in login.get_error_message()
        
        # Escenario 2: Validación de campos vacíos (Obligatorios)
        driver.refresh()
        time.sleep(1)
        login.login_to_app("", "")
        time.sleep(2)
        assert "Username is required" in login.get_error_message()

        # Escenario 3: Login exitoso
        driver.refresh()
        time.sleep(1)
        login.login_to_app("standard_user", "secret_sauce")
        time.sleep(3)
        assert "inventory.html" in driver.current_url
        
        print("Smoke test finalizado con éxito")

    except Exception as e:
        print(f"Test fallido: {e}")
        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    test_saucedemo_smoke()