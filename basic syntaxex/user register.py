# Basic Setting
# Make sure your have project interpreter
# Check Terminal Setting :
# Setting--> Tools --> Terminal --> Shell Path  = "C:\Windows\system32\cmd.exe"
import time

# Install required Library
# pip Install Selenium


# Browser driver run this command --> where python you will get folder where your python is installed Go to scripts
# folder put your driver file to that script folder
# Extract your driver path like this (Example)-- >
# "C:\Users\HP\AppData\Local\Programs\Python\Python311\Scripts\geckodriver.exe"
# we have to set env variable for this path
# for go to Thi Pc --> right click --> Properties --> Control panel home --> Advance System setting -->
# Click on Environment Variables --> in System variables --->Click on Path

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Open Browser
driver = webdriver.Chrome()

# 2. Go To Url --> "https://automation.credence.in"
driver.get("https://automation.credence.in")

# 3. Click on Register link
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()

# Css- CSS stands for cascading style sheets which is the language used to describe the
# HTML pages or you can say use to design the HTML pages. Css
# Format --> tagname[attribute='value'] --> Name CSS --> input[id='name']
# To check CSS in
# browser console --> $$ ('CSS')

# 4. Enter Name
driver.find_element(By.CSS_SELECTOR, "input[id='name'] ").send_keys("Credjuly2")

# XPATH relative format --> //tagname[@attribute='value']
# Email Xpath relative  --> //input[@id='email']
# 5. Enter Email
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Cred@demo3.com")

# 6. Enter Password
driver.find_element(By.ID, "password").send_keys("Cred@123")

# 7. Confirm Password
driver.find_element(By.ID, "password-confirm").send_keys("Cred@123")

# 8. Click On Register Button

driver.find_element(By.CLASS_NAME, "btn").click()

# 9. Validate User Registration
try:
    driver.find_element(By.XPATH, "/html/body/div/div[1]/h2")
    print("User Registration test case is passed")
except:
    print("User Registration test case is failed")

driver.quit()

# Assignment quit vs close difference
# Assignment which is the fastest locator and which is the lowest one and why ?
