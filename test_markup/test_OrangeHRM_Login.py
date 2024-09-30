import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pageobjects.Login_Page import LoginPage_Class

class Test_OrangeHRM_Login:

    def test_OrangeHRM_url_001(self, setup):
        self.driver = setup
        print("driver.title-->" + self.driver.title)
        if self.driver.title == "OrangeHRM":
            assert True
        else:
            assert False
        self.driver.quit()

    def test_OrangeHRM_Login_002(self, setup):
        self.driver = setup
        self.lp = LoginPage_Class(self.driver)
        time.sleep(4)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.lp.Enter_UserName("Admin")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.lp.Enter_Password("admin123")
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.lp.Click_LoginButton()
        if self.lp.Validate_Login_Stauts() == "LoginPass":
            self.lp.Click_Menu_Button()
            self.lp.Click_Logout_Button()
            assert True
        else:
            assert False

        self.driver.quit()
