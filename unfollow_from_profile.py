import self as self
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

wait_time = 20
cooldown_time = 5
correct_email = "m.yasseroaf@gmail.com"
correct_password = "oxsrakas1998"
user_search = "football"

chrome_driver_path = ".\chromedriver.exe"
self.driver = webdriver.Chrome(chrome_driver_path)

self.driver.get("https://www.flickr.com")  # getting flicker.com
self.driver.maximize_window()  # maximize window

login_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[2]/a")))
login_button.click()  # pressing on the login tab

email_textbox = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[2]/div/input")))
email_textbox.send_keys(correct_email)  # sending email to text box

next_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/button")))
next_button.click()  # pressing on next button

password_textbox = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[3]/div/div/input")))
password_textbox.send_keys(correct_password)  # sending password to text box

signin_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/button/span")))
signin_button.click()

time.sleep(cooldown_time)

time.sleep(cooldown_time)
my_profile_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[4]/div/div/div/a")))
my_profile_button.click()
time.sleep(cooldown_time)
into_my_profile = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/section[1]/h4/a")))
into_my_profile.click()

following_window = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/div[3]/div[2]/p[2]/a[2]")))
following_window.click()

user_profile = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/table[2]/tbody/tr[1]/td[2]/a[1]")))
user_profile.click()

press_on_following = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/div[2]/div[1]/div[1]/button")))
press_on_following.click()

unfollow = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div/div/ul/li[4]/button")))
unfollow.click()

#/html/body/div[1]/div/main/div[3]/div/div[2]/div[1]/div/div/a
#Conadeip Premier



