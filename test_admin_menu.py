import pytest
from selenium import webdriver
from pageObjects.admin_menu import AdminMenuPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAdminMenuPage:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.admin_menu = AdminMenuPage(self.driver)
        yield
        self.driver.quit()

    def test_header_validation(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.admin_menu.login("Admin", "admin123")

        #Wait for the header to be clickable
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//li[1]//a[1]//span[1]"))).click()

        # Validate Title of the page
        assert self.admin_menu.validate_title() == "OrangeHRM", "Title validation failed."

        # Validate Admin Menu Items
        actual_menu_items = self.admin_menu.validate_admin_menu_items()
        expected_menu_items = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Claim', 'Buzz']

        assert actual_menu_items == expected_menu_items, "Admin Menu Items validation failed."