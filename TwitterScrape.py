import selenium
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

login_name = os.getenv('USERNAME')
login_password = os.getenv('PASSWORD')

driver = webdriver.Firefox()
driver.get("https://twitter.com/login")

sleep(3)
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys(login_name)
next_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(login_password)
log_in = driver.find_element(By.XPATH, "//span[contains(text(), 'log in')]")
log_in.click()


