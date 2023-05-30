import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Test scenario untuk test login
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    
    # Login berhasil menggunakan data username & password valid
    def test_login_berhasil(self):
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        confirm_heading = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[1]/div[2]/div').text
        self.assertIn("Swag Labs", confirm_heading)

    # Login gagal menggunakan data username & password tidak valid
    def test_login_gagal_1(self):
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("")
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("")
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        error_message = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
        self.assertIn("Epic sadface: Username is required", error_message)

    # Login gagal menggunakan username saja (tanpa password)
    def test_login_gagal_2(self):
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        error_message = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
        self.assertIn("Epic sadface: Password is required", error_message)

    # Login gagal menggunakan password yang salah
    def test_login_gagal_3(self):
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("hello world")
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        error_message = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
        self.assertIn("Epic sadface: Username and password do not match any user in this service", error_message)

if __name__ == '__main__':
    unittest.main()