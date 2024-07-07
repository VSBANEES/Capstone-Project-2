import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pageObjects.forgotpwd_page import ForgotpwdPage

class TestForgotPwd:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.forgotpwd_page = ForgotpwdPage(self.driver)
        self.forgotpwd_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield
        self.driver.quit()

    def test_forgot_password_link_validation(self, setup):
        # Click on "Forgot Password" link
        self.forgotpwd_page.click_forgot_password()

        # Provide username and reset password
        self.forgotpwd_page.provide_username_and_reset_password("Admin")

        # Verify successful message
        success_message = self.forgotpwd_page.get_reset_password_success_message()
        assert "Reset Password link sent successfully" in success_message, "Reset Password link not sent successfully."