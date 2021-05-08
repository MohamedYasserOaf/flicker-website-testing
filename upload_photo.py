import self as self
import pyautogui
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

# my_profile_button = WebDriverWait(self.driver, wait_time).until(
#   EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[4]/div/div/div/a")))
# my_profile_button.click()
# time.sleep(cooldown_time)

upload_button_outside = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[2]/a/i")))
upload_button_outside.click()

choose_photo_video = WebDriverWait(self.driver, 20).until(
    EC.presence_of_element_located(
        (By.ID, "choose-photos-and-videos")))
choose_photo_video.send_keys("C:/Users/myass/Desktop/monarch.png")

confirm_upload = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div[2]/div/div/div[4]/div[1]/div[1]/input")))
confirm_upload.click()

confirm_upload_again = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[14]/div/div/div/div[2]/div[2]/div[2]/input[1]")))
confirm_upload_again.click()


