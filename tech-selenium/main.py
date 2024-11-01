import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from hsuBug.functions import getEnv
from data import findAnswer

load_dotenv()

browser = webdriver.Chrome()

browser.get(getEnv("URL"))
time.sleep(1)

loginBtn = browser.find_element(By.CLASS_NAME, "auth-button")
loginBtn.send_keys(Keys.RETURN)

time.sleep(1)

email = browser.find_element(By.ID, "email")
password = browser.find_element(By.ID, "password")
email.send_keys(getEnv("EMAIL"))
password.send_keys(getEnv("PASSWORD"))
loginSubmit = browser.find_element(By.ID, "sign-action")
loginSubmit.send_keys(Keys.RETURN)

time.sleep(2)

mid = browser.find_element(By.XPATH, "//a[@href='main/mid.html']")
mid.click()
time.sleep(1)

midworrtech = browser.find_element(By.XPATH, "//a[@href='midworrtech.html']")
midworrtech.click()
time.sleep(1)

midtech = browser.find_element(By.XPATH, "//a[@href='sys/midtech.html']")
midtech.click()
time.sleep(2)

questions = browser.find_elements(By.CSS_SELECTOR, ".question > strong")
questions = [q.text for q in questions]
for question in questions:
    try:
        answer = findAnswer(question)
        radio_button = browser.find_element(
            By.CSS_SELECTOR, f'input[type="radio"][value="{answer}"]'
        )
        radio_button.click()
        time.sleep(0.5)
    except:
        pass
time.sleep(1)

submitBtn = browser.find_element(By.ID, "submitBtn")
submitBtn.send_keys(Keys.RETURN)
time.sleep(60)

browser.quit()