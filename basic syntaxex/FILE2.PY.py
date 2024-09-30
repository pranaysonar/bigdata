# 1. Open Browser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# 2. Go To Url --> "https://automation.credence.in"
driver.get("https://automation.credence.in")
# 3. Click on Register link
# driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
import time
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[4]/a").click()
# 4. Enter Name
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[id='name'] ").send_keys("Cred1234")
# XPATH relative format --> //tagname[@attribute='value']
# Email Xpath relative  --> //input[@id='email']
# 5. Enter Email
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("abcd@15.com")
time.sleep(2)
# 6. Enter Password
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("abcd12345")

# 7. Confirm Password
time.sleep(2)
driver.find_element(By.ID, "password-confirm").send_keys("abcd12345")

# 8. Click On Register Button
time.sleep(2)
driver.find_element(By.CLASS_NAME, "btn").click()

# 9. Validate User Registration
try:
    driver.find_element(By.XPATH, "/html/body/div/div[1]/h2")
    print("User Registration test case is passed")
except:
    print("User Registration test case is failed")
















