import selenium
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("https://twitter.com/login")
sleep(3)
username = driver.find_element(By.XPATH, "//input[@name='text']")
