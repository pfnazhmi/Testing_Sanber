import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        # steps
        browser = self.browser  # buka web browser
        # buka situs
        browser.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        browser.find_element(
            By.ID, "txt-username").send_keys("John Doe")  # isi username
        browser.find_element(By.CSS_SELECTOR, "input#txt-password.form-control").send_keys(
            "ThisIsNotAPassword")  # isi password
        # klik tombol sign in
        browser.find_element(By.ID, "btn-login").click()

        # Validasi
        wait = WebDriverWait(browser, 10)
        wait.until(EC.url_contains(
            "https://katalon-demo-cura.herokuapp.com/#appointment"))

        response_data = browser.current_url
        self.assertIn('appointment', response_data)

    def test_a_fail_login_with_wrong_usernameAndPass(self):
        # steps
        browser = self.browser  # buka web browser
        # buka situs
        browser.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        browser.find_element(
            By.ID, "txt-username").send_keys("pfnazhmi")  # isi username
        browser.find_element(By.CSS_SELECTOR, "input#txt-password.form-control").send_keys(
            "isPass?")  # isi password
        # klik tombol sign in
        browser.find_element(By.ID, "btn-login").click()

        # Validasi
        response_message = browser.find_element(
            By.CSS_SELECTOR, "p.lead.text-danger").text
        self.assertEqual(
            response_message, 'Login failed! Please ensure the username and password are valid.')

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
