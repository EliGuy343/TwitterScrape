import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

subject = 'Benjamin Netanyahu'

login_name = os.getenv('USERNAME')
login_password = os.getenv('PASSWORD')

driver = webdriver.Firefox()
driver.get("https://twitter.com/login")

sleep(3)
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys(login_name)
next_button = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(login_password)
log_in = driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]")
log_in.click()

sleep(4)
search_box = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
search_box.send_keys(f'"{subject}"')
search_box.send_keys(Keys.ENTER)


sleep(3)
latest = driver.find_element(By.XPATH, f"//span[contains(text(), 'Latest')]")
latest.click()


tweets = []
while True:
    sleep(3)
    tweets_fetch = driver.find_elements(
        By.XPATH, ".//div[@data-testid='tweetText']")

    for tweet in tweets_fetch:
        tweets.append(tweet.text)
    if len(tweets) > 250:
        break
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')


df = pd.Series(tweets).to_frame()
df.to_csv("tweets.csv")
