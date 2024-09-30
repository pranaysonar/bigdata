import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_argument("headless")

class Test003:

    def CredenceSite_010(self):

        driver = webdriver.Chrome()
        #driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://credence.in/")
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        List = []
        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//a"))
        # print(l)

        time.sleep(2)
        for r in range(1, l + 1):
            Contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//a[" + str(
                r) + "]").text
            # print(Contact)
            List.append(Contact)

        print(List)

        Number = "+91 7391053250"

        if Number in List:
            print(List.index(Number))
            print("Number found--> Position -->" + str((List.index(Number) + 1)))
            assert True
        else:
            print("Number Not Found")
            assert False

        driver.quit()

    # def test_addemo_orange_hrm(self):
    #     driver = webdriver.Chrome(options=chrome_options)
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    #     driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    #     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
    #     driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
    #     driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Rahul")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("H")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Patil")
    #     time.sleep(3)
    #     file = r"C:\Users\HP\Pictures\background.jpg"
    #     driver.find_element(By.XPATH, "//input[@type='file']").send_keys(r"C:\Users\HP\Pictures\background.jpg")
    #     time.sleep(4)
    #     driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     success_msg = driver.find_element(By.XPATH,
    #                                       "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']").text
    #     print(success_msg)
    #     if success_msg == "Successfully Saved":
    #         print("Add employee test case is passed")
    #     else:
    #         print("Add employee test case is failed")
    #
    #     driver.quit()


