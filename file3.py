
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time
# # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# # time.sleep(30)
# # driver.get("https://www.facebook.com/")
#
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# import time
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# time.sleep(5)
# driver.get("https://www.facebook.com/"
#
import time

from selenium import webdriver
#driver = webdriver.Firefox()
#time.sleep(10)
#driver.get("https://www.facebook.com/")

from selenium import webdriver
driver = webdriver.Firefox()
# 2. Go To Url --> "https://automation.credence.in"
driver.get("https://automation.credence.in")
