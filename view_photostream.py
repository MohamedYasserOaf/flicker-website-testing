import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

wait_time = 20
cooldown_time = 5
correct_email = "m.yasseroaf@gmail.com"
correct_password = "oxsrakas1998"

chrome_driver_path = ".\chromedriver.exe"
self.driver = webdriver.Chrome(chrome_driver_path)
self.driver.get("https://www.flickr.com/people/192849838@N04/")
photostream_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/ul/li[2]/a")))
photostream_button.click()
time.sleep(5)

self.driver.get("https://www.flickr.com")
self.driver.maximize_window()
login_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[2]/a")))
login_button.click()

email_textbox = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[2]/div/input")))
email_textbox.send_keys(correct_email)
next_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/button")))
next_button.click()
password_textbox = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[3]/div/div/input")))
password_textbox.send_keys(correct_password)
signin_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/button/span")))
time.sleep(cooldown_time)
signin_button.click()
time.sleep(cooldown_time)
my_profile_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[4]/div/div/div/a")))
my_profile_button.click()
time.sleep(cooldown_time)
into_my_profile = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/section[1]/h4/a")))
into_my_profile.click()
photostream_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/ul/li[2]/a")))
photostream_button.click()
