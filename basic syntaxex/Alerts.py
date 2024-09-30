import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
# alert
time.sleep(3)
alert = Alert(driver).text
print(alert)
# # click on ok
time.sleep(3)
Alert(driver).accept()
success_msg = driver.find_element(By.XPATH, "//p[@id='result']").text
print(success_msg)
#
# # Confirmation Alert
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
time.sleep(3)
#
alert = Alert(driver).text
print(alert)
# # click on ok
time.sleep(3)
#
# # Accept
Alert(driver).accept()
#
# # Dismiss
# #Alert(driver).dismiss()
#
success_msg = driver.find_element(By.XPATH, "//p[@id='result']").text
print(success_msg)
#
#
# #Alert Prompt
#
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(3)
#
alert = Alert(driver).text
print(alert)
# # click on ok
time.sleep(3)
#
# # Prompt
Alert(driver).send_keys("Hi, I'm Rahul")
time.sleep(3)
Alert(driver).accept()
success_msg = driver.find_element(By.XPATH, "//p[@id='result']").text
print(success_msg)
#
# time.sleep(2)
# driver.quit()

