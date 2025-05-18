import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestLoginUI(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        html_path = "file://" + os.path.abspath("ui_tests/mock_login.html")
        self.driver.get(html_path)

    def test_login_invalid_user(self):
        self.driver.find_element(By.ID, "username").send_keys("wronguser")
        self.driver.find_element(By.ID, "password").send_keys("wrongpass")
        self.driver.find_element(By.ID, "login").click()
        error = self.driver.find_element(By.ID, "error").text
        self.assertIn("Invalid", error)

    def tearDown(self):
        self.driver.quit()
