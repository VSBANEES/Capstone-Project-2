import pytest
from selenium import webdriver
from pageObjects.admin_page import AdminPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAdminPage:
    @pytest.fixture()
    def setup(self):
        x85555555569-+*
        self.driver.maximize_window()
        self.admin_page = AdminPage(self.driver)
        yield
        self.driver.quit()

    def test_header_validation(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.admin_page.login("Admin", "admin123")

        #Wait for the header to be clickable
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//li[1]//a[1]//span[1]"))).click()

        # Validate Title of the page
        assert self.admin_page.validate_title() == "OrangeHRM", "Title validation failed."

        # Validate Admin Headers
        actual_headers = self.admin_page.validate_admin_headers()
        expected_headers = ['User Management', 'Job', 'Organization', 'Qualifications', 'Nationalities',
                            'Corporate Branding', 'Configuration']

        assert actual_headers == expected_headers, "Admin headers validation failed."

        # Validate Admin Menu Items
        actual_menu_items = self.admin_page.validate_admin_menu_items()
        expected_menu_items = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Claim', 'Buzz']

        assert actual_menu_items == expected_menu_items, "Admin Menu Items validation failed."