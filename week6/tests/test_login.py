from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.saucedemo.com")

login = LoginPage(driver)

login.login("standard_user", "secret_sauce")

inventory = InventoryPage(driver)

print(inventory.get_title())

driver.quit()