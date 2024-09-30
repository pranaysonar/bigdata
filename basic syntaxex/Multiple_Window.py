import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']").click()

# capture all the windows in browser
#driver.window_handles
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
text1 = driver.find_element(By.XPATH, "//div[@class='large-4 large-centered columns']//div[1]").text
print(text1)
# #Powered by Elemental Selenium
#
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
text2 = driver.find_element(By.XPATH, "//h3[normalize-space()='New Window']").text
#
print(text2)
# # New Window
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
#driver.close()
driver.quit()
# try this code with both close and quit